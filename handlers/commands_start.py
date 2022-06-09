from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
import asyncio

ids_user = []
markup = types.InlineKeyboardMarkup()

bat_1 = types.InlineKeyboardButton(text='ВПИСКИ (102 гб) | 99.00 RUB', callback_data='bat_1')
bat_2 = types.InlineKeyboardButton(text='СКРЫТЫЕ КАМЕРЫ (235 гб) | 149.00 RUB', callback_data='bat_2')
bat_3 = types.InlineKeyboardButton(text='VIP КОНТЕНТ (312 гб) | 199.00 RUB', callback_data='bat_3')
bat_4 = types.InlineKeyboardButton(text='🏆🤑Всё вместе🤑🏆 (выгодно) | 249.00 RUB', callback_data='bat_4')

markup.add(bat_1)
markup.add(bat_2)
markup.add(bat_3)
markup.add(bat_4)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(id = message.chat.id)
    await message.answer(text="""<b>💙💦VIP ДОСТУП💦💙

▪️Автоматический бот🤖✅ 

▪️Анонимная покупка🤫✅

▪️Моментальный доступ 😋✅

✅СКИДКА 50% ДО КОНЦА МЕСЯЦА

Выберите желаемый товар или категорию: 👇🏽👇🏽👇🏽</b>""",reply_markup=markup)