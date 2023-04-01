## Environment Setup

conda create -n algo-oanda-demo-py38 python=3.8

conda activate algo-oanda-demo-py38

pip install -r requirements.txt

pip install git+https://github.com/happydasch/btoandav20

### remove conda env

conda deactivate

conda env remove -n algo-oanda-demo-py38

## Docker
### build docker image
* docker build --tag algo-oanda-demo .

### manage docker images
* docker images
* docker tag algo-oanda-demo:latest algo-oanda-demo:v1.0.0
* docker rmi algo-oanda-demo:v1.0.0

### run/stop docker images
* docker run -d --name algo-1 algo-oanda-demo
    * `-d` is detached for running in background
    * `--name` is to give the container a name
* docker ps -a
* docker stop algo-1
* docker restart algo-1
* docker rm algo-1

## Push to AWS
View "Push Instruction" from AWS ECR web console.