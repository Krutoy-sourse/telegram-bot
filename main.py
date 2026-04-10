from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from random import randint
import os

TOKEN = os.getenv(8266023377:AAHr4maCljTr1CXp5HE2LTIN2j7rXKdnmNU)

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['roll'])
async def roll(message: types.Message):
    await message.answer(str(randint(1, 6)))


@dp.message_handler(commands=['credits'])
async def credits(message: types.Message):
    await message.answer("Created by Krico Mucaci")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)  
