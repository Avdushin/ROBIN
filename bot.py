from email import message
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv
from dispatcher import bot, dp
from msgs import *

import logging, asyncio, emoji, os

# Find .env file
load_dotenv(find_dotenv())

# Bot start
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)