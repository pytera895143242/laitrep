from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import random

Price1 = 99
Price2 = 149
Price3 = 199
Price4 = 249


content_chat = -1001780671252

url = 'https://oplata.qiwi.com/create?'
key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPv6ZGxcKa57QVtRzoXj1NRj7uZrTsteoe44Ec5UtXeY5A4N1EimwxZPr9LPWuZgKKrTwzrkDTwuTN8KS6CZtQdFn8j3GEcv4wveejYe3zT'


@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat_exit = types.InlineKeyboardButton(text='👈 НАЗАД', callback_data='bat_exit')

    if call.data == 'bat_1':
        price = f'&amount={Price1}'
        finish_url = url+key+price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url = finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await call.message.answer(text =  """<b>Тариф:</b> ВПИСКИ (102 гб)
<b>Цена:</b> 99.00 RUB
<b>Срок:</b> Бессрочный""",reply_markup=markup)


    if call.data == 'bat_2':
        price = f'&amount={Price2}'
        finish_url = url + key + price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await call.message.answer(text="""<b>Тариф:</b> СКРЫТЫЕ КАМЕРЫ (235 гб)
<b>Цена:</b> 149.00 RUB
<b>Срок:</b> Бессрочный""", reply_markup=markup)

    if call.data == 'bat_3':
        price = f'&amount={Price3}'
        finish_url = url + key + price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await call.message.answer(text="""<b>Тариф:</b> VIP КОНТЕНТ (312 гб)
<b>Цена:</b> 199.00 RUB
<b>Срок:</b> Бессрочный""", reply_markup=markup)

    if call.data == 'bat_4':
        price = f'&amount={Price4}'
        finish_url = url + key + price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url=finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await call.message.answer(text="""<b>Тариф:</b> 🏆🤑Всё вместе🤑🏆 (выгодно)
<b>Цена:</b> 249.00 RUB
<b>Срок:</b> Бессрочный""", reply_markup=markup)

    if call.data == 'bat_exit':
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)


    await bot.answer_callback_query(callback_query_id=call.id)