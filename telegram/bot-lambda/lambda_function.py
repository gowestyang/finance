import json
from botocore.vendored import requests

TELEGRAM_TOKEN = '6252951396:AAHAYGHvDR_r1TKmC1x9Exxs93ygYJf8sPU'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

def send_telegram_message(text, chat_id):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(TELEGRAM_API_URL + 'sendMessage', data=payload)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    text = message['message']['text']

    # echo back
    send_telegram_message('You said: '+text, chat_id)
    return {
        'statusCode': 200
    }
