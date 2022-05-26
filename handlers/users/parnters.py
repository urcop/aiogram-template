from aiogram import types

from loader import dp, change_lang, db, __


@dp.message_handler(text=change_lang('Партнерская структура'))
async def partners(message: types.Message):
    referals = await db.count_refs(message.from_user.id)
    lang = await db.language(message.from_user.id, take=True)
    earn = await db.get_earn(message.from_user.id)
    text = [__(f'<b>{i + 1}-я линия</b> -', src='ru', dest=lang).text + ' ' + str(
        referals[i]) + ' ' + __('партнеров', src='ru', dest=lang).text for i in
            range(0, 5)]
    text.append(__(f'Заработано всего - {earn} USDT', src='ru', dest=lang).text)
    await message.answer('\n'.join(text))
