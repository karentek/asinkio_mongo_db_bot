import os
from dotenv import load_dotenv, find_dotenv
from pymongo.server_api import ServerApi
import os
from pymongo import MongoClient
import logging
from aiogram import Bot


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
URI = os.getenv('URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION = os.getenv('COLLECTION')
CLIENT = MongoClient(URI, server_api=ServerApi('1'))
DB = CLIENT[DB_NAME]
COLLECTION = DB[COLLECTION]
bot = Bot(token=BOT_TOKEN)


if URI is None:
    raise ValueError("MONGO_URI environment variable is not set")
logger.info('Send a ping to confirm a successful connection with MongoDB - Atlas')
try:
    CLIENT.admin.command('ping')

    logger.info("Pinged. You successfully connected!")
except Exception as e:
    logger.info(f'{e}')

