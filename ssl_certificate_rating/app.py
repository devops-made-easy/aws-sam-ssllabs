import json
import requests
import time
import os

def send_slack_message(content):
    webhook = os.environ['SLACK_WEBHOOK_URL']
    payload = {
        "attachments": content
    }
    requests.post(webhook,
                  json.dumps(payload),
                  headers={'content-type': 'application/json'})

def lambda_handler(event, context):
    name = os.environ['DOMAIN']
    url = f"https://api.ssllabs.com/api/v3/analyze?host={name}"
    print(f"RUNNING SSL SCAN ON : {name}")
    try:
        data = requests.get(url).json()
        status = data['status']
        count = 0
        while status != "READY":
            count = count + 1
            # Wait for 5 seconds
            print(f"{count}. NOT READY YET ....")
            time.sleep(10)
            data = requests.get(url).json()
            status = data['status']
        report_link = f"https://www.ssllabs.com/ssltest/analyze.html?d={name}"
        title = { "pretext" : f"*SSL Report for * {name} \n <{report_link}|Click Me! for Detailed Report> \n Resolves to following Endpoints"}
        result = []
        result.append(title)
        for endpoint in data['endpoints']:
            print(endpoint)
            color_code = "#E01E5A"
            if endpoint['grade'] == "A" or endpoint['grade'] == "A+":
                color_code = "#2EB67D"
            grade = { "color" : color_code, "author_name" : endpoint['ipAddress'] , "title" : f"Grade: {endpoint['grade']}"}
            result.append(grade)

        send_slack_message(result)
        status_code = 200
        message = "SSL SCAN COMPLETE"
        # send_email(name, content)
        # with open('/tmp/output.html', 'w') as f:
        #     f.write(content)

    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)
        status_code = "400"
        message = "DID NOT RUN AS EXPECTED"
        raise e

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message
        }),
    }
