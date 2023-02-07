from aiogram import Bot, Dispatcher, executor, types
from random import choice
from config import TOKEN
from funny_cat import emoji_cat
import logging

"""
Задачи!!

1.Реализуйте бота который будет отправлять стикер с котиком в ответ на команду /give,но перед этим
он должен отправить сообщения "Смотри какой смешной кот и ❤️ "
2.Модифицируйте бота который отправляет черное сердечко в ответ на крастрое
3.Реализуйте бота который будет прочитывать количество  ✔️ и возвращать их пользователю
4.Напишите функуию /help которая будет возвращать список существующих команд,отформатировать так чтобы список команд
были жирным шрифтом а описание курсивом
5.Напишите функцию on_startup() ,которая будет выводить Я запустился!
6.Напишите функцию который будет отправлять id стикера в ответ пользователю!

"""
HELP_COMMAND = """
<b>/help</b> - <em>список существующих команд</em>
<b>/start</b> - <em>start bot</em>
<b>/give</b> - <em>возвращает смешного кота</em>

"""

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
db = Dispatcher(bot)


async def on_startup(_):
    print("Я запустился")


@db.message_handler(commands=["help"])
async def send_help(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")


@db.message_handler(commands=["give"])
async def send_heart(message: types.Message):
    await message.answer(text=F"Смотри какой смешной кот  ❤️")
    await bot.send_sticker(message.from_user.id, sticker=choice(emoji_cat))


# @db.message_handler()
# async def send_help(message: types.Message):
#     await message.reply(text=F"Количество ✔️ в сообщении  == {message.text.count('✔️')}")
#

# @db.message_handler()
# async def a_parrot(message: types.Message):
#     if message.text == "❤️":
#         await message.answer(text="💋")
#     else:
#         await message.answer(text="Попробуй отправить мне сердечко!)")


@db.message_handler(content_types=['sticker'])
async def send_check_id_sticker(message: types.Message):
    await message.answer(text=F"{message.sticker.file_id}")


executor.start_polling(db, skip_updates=True, on_startup=on_startup)
