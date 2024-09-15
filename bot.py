from aiogram import Bot, Dispatcher, types 
from aiogram.filters.command import Command
import asyncio
import logging 
from calculation import price_BTC_usd, price_BTC_rub
with open('token.txt', 'r', encoding='utf-8') as f:
    token_bot = f.read(46)

logging.basicConfig(level=logging.INFO)
bot_token = Bot(token=token_bot)
dp = Dispatcher()
# text_price = (f"Отлично! Цена Bitcoin составляет: \n**{price_BTC_rub()}**₽ рублей. \n**{price_BTC_usd()}**$ долларов.", parse_mode="Markdown")
@dp.message(Command("start"))
async def async_start(message:types.Message):
    await message.answer("Здравствуйте! Данный бот создан для того, чтобы предоставлять информацию о курсе Bitcoin. Для того чтобы узнать текущий курс, используйте команду /price.")

@dp.message(Command("price"))
async def async_start(message:types.Message):
    await message.answer(f"Отлично! Цена Bitcoin составляет: \n<b>{price_BTC_rub()}</b>₽ рублей. \n<b>{price_BTC_usd()}</b>$ долларов.", parse_mode="html")
async def main():
    await dp.start_polling(bot_token)

if __name__ == "__main__" :
    asyncio.run(main())

