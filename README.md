# serverless-ssllabs
==============

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-orange.svg)](https://sonarcloud.io/dashboard?id=devops-made-easy_aws-sam-ssllabs)

AWS SAM Project for the Qualys SSL Labs API. Idea behind this project is to run ssl scans on a specific schedule and send ratings as slack message.

## Features

* Scans SSL Grade and send as a Slack Message.


The application uses several AWS resources, including Lambda functions and CloudWatch Event. These resources are defined in the `template.yaml` file in this project. 

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

Run functions locally and invoke them with the `sam local invoke` command.

```bash
AWS$ sam local invoke HelloWorldFunction --event events/event.json
```

## Terms of Use

This is not an official SSL Labs project. Please make sure to read the official [Qualys SSL Labs Terms of Use](https://www.ssllabs.com/downloads/Qualys_SSL_Labs_Terms_of_Use.pdf).

Also you should

* only inspect sites and servers whose owners have given you permission to do so.
* be clear that this tool works by sending assessment requests to remote SSL Labs servers and that this information will
be shared with them.



