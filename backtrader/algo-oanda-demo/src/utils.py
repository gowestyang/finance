import logging
import json
import requests

# logger
LOGGING_FORMAT = "[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"
LOGGING_LEVEL = logging.INFO
logging.basicConfig(format=LOGGING_FORMAT, level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)

# telegram
TELEGRAM_CONFIG_FILE = 'src/config/telegram.json'
with open(TELEGRAM_CONFIG_FILE) as f:
    d_telegram_config = json.load(f)

# Function to send a message to telegram
def send_telegram(text: str) -> requests.models.Response:
    response = requests.get(
        f"https://api.telegram.org/bot{d_telegram_config['telegram_api']}/sendMessage",
        {
            'chat_id': d_telegram_config['telegram_chat_id'],
            'text': text
        })
    
    return response

# Function to log and send a message to telegram
def send_log(txt: str, level=logging.INFO) -> None:

    logger.log(msg=txt, level=level)
    
    if level > logging.DEBUG:
        response = send_telegram(txt)
        if response.status_code != 200:
            logger.log(f"WARNING: failed to send message to telegram: {response.text}", level=logging.warning)
