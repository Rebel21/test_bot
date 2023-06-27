import logging
import os

from aiogram import Bot, Dispatcher, types, executor

bot = Bot(os.environ.get('BOT_TOKEN'))
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['ping'])
async def ping_handler(message: types.Message):
    logging.info(message.text)
    await message.answer('pong')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)