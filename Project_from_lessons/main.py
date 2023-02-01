from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import TOKEN
from stikers_cat import emoji_cat
from random import choice
from keyboards import kb, kb_photo, kb_joke
from help_command import HELP_COMMAND
from parse_photo import smile
from parse_joke import jokes
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
db = Dispatcher(bot)

new_smile_photo = smile.copy()
new_jokes = jokes.copy()


async def on_start_up(_):
    print("Готов к работе")


@db.message_handler(Text(equals="Давай начнем 🤙"))
async def command_start(message: types.Message):
    await message.answer(
        text=F"Привет 🥳"
             F"зайди ко мне  ➡️ @Good_teletele_bot И начнем общаться ✅"
        ,
    reply_markup=kb)
    await message.delete()


@db.message_handler(Text(equals="Help 🆘"))
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@db.message_handler(Text(equals="giv_cat 😽"))
async def giv_cat(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=F"Смотри какой смешной кот 😽"
                           )
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=choice(emoji_cat))
    await message.delete()


@db.message_handler(Text(equals="description 👀"))
async def command_descriptions(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHh7Fj2Sf4gLEBGA7xgulqRXnzsCXGPwACCwMAAm2wQgN_tBzazKZEJS0E')
    await bot.send_message(chat_id=message.from_user.id,
                           text=F"Для тебя  {message.from_user.full_name} Я покорный слуга!))")
    await message.delete()


@db.message_handler(Text(equals="random_photo 🎲"))
async def random_photo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=F"Что-бы отправить рандомную фотографию нажми 'Рандом🎲' "
                                F"Что-бы выйти нажмите Меню⏪",
                           reply_markup=kb_photo)
    await message.delete()


@db.message_handler(Text(equals="Меню⏪"))
async def open_kb_menu(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=F"Добро пожаловать в Главное Меню ✅",
                           reply_markup=kb)
    await message.delete()


@db.message_handler(Text(equals="Рандом🎲"))
async def open_random_photo(message: types.Message):
    global new_smile_photo
    try:
        if new_smile_photo:
            await bot.send_message(chat_id=message.from_user.id,
                                   text=F"Вот поори с этих идиотов)))"
                                        F"Осталось {len(new_smile_photo)} фотографий 📷",
                                   reply_markup=kb_photo)

            await bot.send_photo(chat_id=message.from_user.id,
                                 photo=new_smile_photo[0])
            await message.delete()

            del new_smile_photo[0]

        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text=F"Пожалуй пока все оствлось {len(new_smile_photo)} фотографий 📷"
                                        F"Если хочешь можешь начать заново😂 нажми random_photo 🎲",
                                   reply_markup=kb)
            new_smile_photo = smile.copy()

    except IndexError as err:
        print("list index out of range",err)
@db.message_handler(Text(equals="Хочу анекдот 🫰"))
async def open_random_jokes(message: types.Message):
    global new_jokes
    if new_jokes:
        await bot.send_message(chat_id=message.from_user.id,
                               text=F"Ну лови 🙌 😛😛😛\n"
                                    F"\n"
                                    F"{new_jokes[0]}",
                               reply_markup=kb_joke)

        await message.delete()

        del new_jokes[0]

    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=F"Пожалуй пока все оствлось {len(new_jokes)} анекдотов 😂"
                                    F"Если хочешь можешь начать заново😂 нажми jokes 😂",
                               reply_markup=kb)
        new_jokes = jokes.copy()


@db.message_handler(Text(equals="jokes 😂"))
async def random_photo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=F"Что-бы отправить анекдот нажмите Хочу анекдот 🫰 \n "
                                F"Что-бы выйти нажмите Меню⏪",
                           reply_markup=kb_joke)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True,
                           on_startup=on_start_up)
