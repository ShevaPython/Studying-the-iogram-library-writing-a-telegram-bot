# from aiogram import Bot, types, executor, Dispatcher
# from config import TOKEN
# import logging
#
# # 1.Напишите бота который будет отправлять его же сообщения,переведенное в верхний регистер!
# # 2.Напишите бота который будет отправлять его же сообщения,если сообщения состоит более чем 2 слова!
#
# API_TOKEN = TOKEN
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# db = Dispatcher(bot)
#
#
# @db.message_handler()
# async def echo(message: types.Message):
#     if message.text.count(" ") == 0:
#         await message.answer(text=F"Эй ты чего {message.from_user.first_name} напиши больше чем 2 слова"
#                                  F"И я сделаю их в верхнем регистре!")
#
#     else:
#         await message.answer(text=F"{message.from_user.first_name} вот твое слово в верхнем регистре"
#                                   F" ->>   yes"
#                                   F"{message.text.upper()}")
#
#
# executor.start_polling(db, skip_updates=True)
