from aiogram import types

from loader import dp, change_lang


@dp.message_handler(text=change_lang('Партнерская структура'))
async def partners(message: types.Message):
    text = ''
    await message.answer(text)