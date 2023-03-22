## Docker
### build docker image
* `docker build --tag telegram-echo-bot .`

### manage docker images
* `docker images`
* `docker tag echo-bot-docker:latest echo-bot-docker:v1.0.0`
* `docker rmi echo-bot-docker:v1.0.0`

### run/stop docker images
* `docker run -d --name echo-bot-1 echo-bot-docker`
    * `-d` is detached for running in background
    * `--name` is to give the container a name
* `docker ps -a`
* `docker stop echo-bot-1`
* `docker restart echo-bot-1`
* `docker rm echo-bot-1`
