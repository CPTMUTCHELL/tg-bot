from aiogram import types
from aiogram.types.web_app_info import WebAppInfo
from decouple import config
async def show_buttons(message: types.Message, message_text: str):
    # one_time_keyboard=True doesn't work with IPhone
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False,resize_keyboard=True)
    order_template_btn = types.KeyboardButton('Заказать', web_app=WebAppInfo(url=config('WEB_APP_URL')))
    reviews_btn = types.KeyboardButton('Отзывы')
    working_hours_btn = types.KeyboardButton('Режим работы магазина')
    markup.add(reviews_btn, order_template_btn, working_hours_btn)
    await message.answer(message_text, reply_markup=markup)
