# from aiogram import Bot, Dispatcher, executor, types
# from inlinekb import kb,ilkm
# import logging
# from config import TOKEN
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(TOKEN)
# db = Dispatcher(bot)
#
# async def start_up(_):
#     print("Я запустился")
#
#
# @db.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Добро пожаловать в главное меню!',
#                            reply_markup=kb)
#
#
# @db.message_handler(commands=["link"])
# async def send_link(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="Выбирите опцию...",
#                            reply_markup=ilkm)
#
#
# if __name__ == "__main__":
#     executor.start_polling(db, skip_updates=True, on_startup=start_up)
