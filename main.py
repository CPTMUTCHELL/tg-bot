import json

import texts
from aiogram import Bot, Dispatcher, executor, types

import asyncio
import logging

from Order import Order
from keyboards import show_buttons
from decouple import config

bot = Bot(config('TOKEN'))
dp = Dispatcher(bot)

async def main():

    await dp.start_polling(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    mess = texts.greeting_message.format(name=message.from_user.first_name)
    await message.answer(mess, parse_mode='html')
    await show_buttons(message, 'Выбери опцию')

@dp.message_handler(content_types=['web_app_data'])
async def get_web_app_data(message: types.Message):
    data = message.web_app_data.data
    customer = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
    data = json.loads(data)
    order = Order(customer, data["city"], data["address"], data["tel_num"], data["volume"], data["brand"],
                  data["aroma"])
    if data.get("promo_code") is not None:
        order.promo_code = data["promo_code"]
    if data.get("message") is not None:
        order.message = data["message"]
    await message.answer('Заказ принят', parse_mode="Markdown")
    await send_msg_to_users(order)

@dp.message_handler()
async def show_reviews(message: types.Message):
    if message.text == 'Отзывы':
        markup = types.InlineKeyboardMarkup()
        reviews_btn = types.KeyboardButton('Отзывы', url='https://t.me/nevoda26_otzivi')
        markup.add(reviews_btn)
        await message.answer('Прочитать отзывы', reply_markup=markup)
async def send_msg_to_users(order: Order):

    for admin_id in texts.admin_ids:
        await bot.send_message(admin_id, str(order), parse_mode="Markdown")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
