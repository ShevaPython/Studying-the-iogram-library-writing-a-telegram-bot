from aiogram import Bot, executor, types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
import logging
from config import TOKEN

"""
Простейшая клавиатура!!

-Каждая встраиваимая клавиатура являеться экземпляром класса ReplyKeyboardMarkup и содержит внутри заданая нами число кнопок!

-Каждая кнопка устанавливаеться посредством методом KeyboardButton(), в которой указываеться конкретная опция,которую
 может выполнить пользователь!

- resize_keyboard=True подстраиваеться под интерфейс телеграмма
- one_time_keyboard=True - при нажатии на команду на клавиатуре,она изщезает!


"""

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
db = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).add(KeyboardButton('/description')).insert(KeyboardButton("/image"))

HELP_COMMAND = """
<b>/help</b> - <em>список существующих команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описания бота</em>
<b>/image</b> - <em>отправляет нашего фото</em>

"""


@db.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML",
                           )
    await message.delete()


@db.message_handler(commands=["start"])
async def send_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=F"Добро пожаловать я Ваш Bot!"
                                F"Если вы хотите что бы я отправлял Вам персональные сообщения "
                                F"Добавь меня  @Good_teletele_bot и нажмите /start",
                           reply_markup=kb)
    await message.delete()


@db.message_handler(commands=["description"])
async def send_description(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=F"Привет {message.from_user.full_name}!\n "
                                F"Посмотри что я умею!",
                           )
    await message.delete()


@db.message_handler(commands=["image"])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://www.pexels.com/ru-ru/photo/14881779/",
                         )


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)
