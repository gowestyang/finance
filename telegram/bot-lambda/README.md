## Steps:
Reference: https://chatbotslife.com/building-a-telegram-bot-with-aws-api-gateway-and-aws-lambda-21ef3239a053

1. In AWS Lambda, create a Lambda function.
2. In AWS API Gateway, deploy a REST API. Link it to the Lambda function.
    * This is needed for telegram to trigger the lambda via webhook.
    * After deployment, note down the invoke URL, such as `https://7qkjt266g7.execute-api.us-east-1.amazonaws.com/v1/`
3. Set webhook to the telegram bot by `https://api.telegram.org/bot<your-bot-token>/setWebHook?url=<your-API-invoke-URL>`
    * For example, `https://api.telegram.org/bot6252951396:AAHAYGHvDR_r1TKmC1x9Exxs93ygYJf8sPU/setWebHook?url=https://7qkjt266g7.execute-api.us-east-1.amazonaws.com/v1/`
    * You can do this simply using a web browser
    * check webhook: `https://api.telegram.org/bot6252951396:AAHAYGHvDR_r1TKmC1x9Exxs93ygYJf8sPU/getWebhookInfo`




## Environment Setup

conda create -n telegram-lambda-py37 python=3.7

conda activate telegram-lambda-py37

**At the deployment-package folder**

pip install --target ./ requests boto3

**zip all contents in the deployment-package folder**

### remove conda env

conda deactivate

conda env remove -n telegram-py38

### test Lambda Package Locally

**At the deployment-package folder**

sam local start-api --template template.yaml

## 
