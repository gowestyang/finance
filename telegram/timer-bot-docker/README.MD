## Docker
### build docker image
* docker build --tag telegram-timer-bot .

### manage docker images
* docker images
* docker tag telegram-echo-bot:latest telegram-echo-bot:v1.0.0
* docker rmi telegram-echo-bot:v1.0.0

### run/stop docker images
* docker run -d --name echo-bot-1 telegram-echo-bot
    * `-d` is detached for running in background
    * `--name` is to give the container a name
* docker ps -a
* docker stop echo-bot-1
* docker restart echo-bot-1
* docker rm echo-bot-1

## Push to AWS
View "Push Instruction" from AWS ECR web console.