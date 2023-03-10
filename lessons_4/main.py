from aiogram import Bot, executor, Dispatcher, types
from jokes import list_jokes
from config import TOKEN
from lessons_3.funny_cat import emoji_cat
from random import choice
import logging

"""
--Администрирование группы
--Отправка местоположений и фотографий
--Для отправки контента пользователю send_something в аргумент чат chat_id в котором указываеться ID чата необходимо
отправлять сообщения
Усли мы хотив отправить сообщения пользователю в личку  используеться bot.send_message(message.from_user.id.)
Еили хотим отправить в групу используем message.chat.id
"""

HELP_COMMAND = """
<b>/help</b> - <em>список существующих команд</em>
<b>/start</b> - <em>start bot</em>
<b>/give</b> - <em>возвращает смешного кота</em>
<b>/image</b> - <em>отправляет фотографию</em>
<b>/location</b> - <em>отправка места локации</em>
<b>/joke</b> - <em>Почитать какойто-анекдок</em>"""

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
db = Dispatcher(bot)


@db.message_handler(commands=["image"])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://ulibky.ru/kartinki/krutye-kartinki-dlya-pacanov-na-avu-v-vk-59-foto.html")
    await message.delete()


@db.message_handler(commands=["location"])
async def send_point(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=F"А вот где я обитаю))")
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=47.2586948,
                            longitude=-119.6341078)
    await message.delete()


@db.message_handler(commands=["help"])
async def send_help(message: types.Message):
    user_id = message.from_id
    await bot.send_message(chat_id=user_id, text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()


@db.message_handler(commands=["start"])
async def send_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=F"Если вы хотите что бы я отправлял Вам персональные сообщения "
                                F"Добавь меня  @Good_teletele_bot и нажмите /start")

    await bot.send_message(chat_id=message.chat.id, text=F"Привет {message.from_user.full_name}!!!!!\n "
                                                         F"Хочешь узнать что я могу нажми команду ->> /help")


@db.message_handler(commands=["give"])
async def send_heart(message: types.Message):
    await message.answer(text=F"Смотри какой смешной кот  ❤️")
    await bot.send_sticker(message.from_user.id, sticker=choice(emoji_cat))


@db.message_handler(commands=['joke'])
async def send_joke(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=F"Что-бы посмеяться напиши -   анекдот")


@db.message_handler(content_types=['text'])
async def send_number_jokes(message: types.Message):
    if message.text.lower() == "анекдот":
        await bot.send_message(chat_id=message.from_user.id, text=F"{list_jokes[0]}")
        del list_jokes[0]
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=F"Смотри какой ты хитрый {message.from_user.full_name} "
                                    F"Давай слово анекдот ")


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)
