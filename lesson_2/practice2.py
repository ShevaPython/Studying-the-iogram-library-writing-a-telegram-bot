from aiogram import Bot, executor, Dispatcher, types
import logging
from config import TOKEN
import string
from random import choice

"""Задачи
1.Напишите бота который будет отвечать на сообщения пользователя рандомным символом алфавита
2.Модифицыруйте бота ,добавив обработки команд /description -- которая будет выводить описания бота!
3.Добавить команду /count которая будет подчитывать количество повторений вызовов 
4.Бот должен отвечать "YES" если вели 0 или "NO" в противном
"""

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - описания бота
/count - подсчет количества раз вызывания команды
"""

alphabet = string.ascii_uppercase

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
db = Dispatcher(bot)
count_message = 0

@db.message_handler(commands=["help"])
async def send_help_commands(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@db.message_handler(commands=["description"])
async def send_description_bot(message: types.Message):
    await message.answer(text=F"Привет, я умею отправлять рандомные символы латинского алфавита!!")
    await message.delete()


@db.message_handler(commands=["count"])
async def send_count(message:types.Message):
    global count_message
    count_message += 1
    await message.reply(text=F"Вот сколько раз ты вызывал команду /count ->> {count_message}")


@db.message_handler()
async def send_random_letter(message: types.Message):
    if message.text != "0":
        await message.reply(text="YES")
    else:
        await message.reply(text="NO")

@db.message_handler()
async def send_random_letter(message: types.Message):
    await message.reply(text=F"На лубое твое сообщения я отправлю тебе рандомную букву алфавита"
                             F" Вот она : ->> {choice(alphabet)} <<-")


executor.start_polling(db, skip_updates=True)
