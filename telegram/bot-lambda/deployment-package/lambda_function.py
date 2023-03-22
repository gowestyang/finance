import json
import boto3
import requests

TELEGRAM_TOKEN = '6252951396:AAHAYGHvDR_r1TKmC1x9Exxs93ygYJf8sPU'
#TELEGRAM_CHAT_ID = '2069686152'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

CLUSTER_NAME = 'bot'
SERVICE_NAME = 'telegram-bot-service'
TASK_DEFINITION = 'mini-fargate'


def send_telegram_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(TELEGRAM_API_URL + 'sendMessage', data=payload)

ecs = boto3.client('ecs')

def start_service():
    ecs.update_service(cluster=CLUSTER_NAME, service=SERVICE_NAME, desiredCount=1)
    return 'Service started.'

def stop_service():
    ecs.update_service(cluster=CLUSTER_NAME, service=SERVICE_NAME, desiredCount=0)
    return 'Service stopped.'

def restart_service():
    stop_service()
    start_service()
    return 'Service restarted.'

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    text = message['message'].get('text', '').strip().lower()

    if text == '/start':
        response = start_service()
    elif text == '/stop':
        response = stop_service()
    elif text == '/restart':
        response = restart_service()
    else:
        response = 'Invalid command. Use /start, /stop, or /restart.'

    send_telegram_message(chat_id, response)
