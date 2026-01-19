import os

import asyncio
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer("Привет! Я эхо-бот!")


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    logger.add('file.log',
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days")

    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
