from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from random import randint
from credits import token

from aiohttp_socks import ProxyConnector
from aiohttp import ClientSession

# 🔐 ВСТАВЬ СЮДА СВОЙ ПРОКСИ
PROXY_URL = "socks5://5.130.4.14:1081"
# пример:
# PROXY_URL = "socks5://user:pass@123.123.123.123:1080"

# создаём подключение через прокси
connector = ProxyConnector.from_url(PROXY_URL)
session = ClientSession(connector=connector)

bot = Bot(token=token, session=session)
dp = Dispatcher(bot)


@dp.message_handler(commands=['roll'])
async def roll(message: types.Message):
    await message.answer(str(randint(1, 6)))


@dp.message_handler(commands=['credits'])
async def credits(message: types.Message):
    await message.answer("Created by Krico Mucaci")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

    