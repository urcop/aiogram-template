from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import __

rent_callback = CallbackData('user', 'rent')


def rent_keyboard(lang):
    result = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(__('1 месяц (30 USDT)', src='ru', dest=lang).text,
                                 callback_data=rent_callback.new('rent1')),
        ],
        [
            InlineKeyboardButton(__('2 месяца (55 USDT)', src='ru', dest=lang).text,
                                 callback_data=rent_callback.new('rent2')),
        ],
        [
            InlineKeyboardButton(__('3 месяца (75 USDT)', src='ru', dest=lang).text,
                                 callback_data=rent_callback.new('rent3')),
        ],
        [
            InlineKeyboardButton(__('Год (200 USDT)', src='ru', dest=lang).text,
                                 callback_data=rent_callback.new('rent12')),
        ],
    ], row_width=1)
    return result


buy_request = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Одобрить', callback_data='buy_accept'),
        InlineKeyboardButton('Отклонить', callback_data='buy_cancel')
    ]
])
