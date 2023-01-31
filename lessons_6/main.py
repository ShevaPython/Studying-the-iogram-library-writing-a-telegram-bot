# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# import logging
# from config import TOKEN
#
# """
# Inline  клавиатура
# - Каждани инлайн клавиатура также будет сбособна обновлять свое содержимое
#   Для создания inline клавиатуры будет использован класс InlineKeyboardMarkup
#
# - Каждая кнопка устанавливаеться посредством метода  InlineKeyboardButton(),в котором указываеться конкретная  опция
#   которую может выполнить  пользователь,а также некоторый функционал по типу url
# """
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(TOKEN)
# db = Dispatcher(bot)
#
# ikb = InlineKeyboardMarkup(row_width=3)
# ibGit = InlineKeyboardButton(text="GIT",
#                              url="https://github.com/ShevaPython")
# ibTelegram = InlineKeyboardButton(text="Telegram",
#                                   url="https://t.me/Sergey_ShevaA")
# ibInstagram = InlineKeyboardButton(text="Instagram",
#                                    url="https://www.instagram.com/shevtsovsn/?igshid=MDM4ZDc5MmU%3D")
# ikb.add(ibTelegram, ibInstagram, ibGit)
#
#
# @db.message_handler(commands=["start"])
# async def send_start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="Пререходите на мой GIT,Telegram,Instagram",
#                            reply_markup=ikb)
#
#
# async def on_startup(_):
#     print("Ready to work")
#
#
# if __name__ == "__main__":
#     executor.start_polling(db, skip_updates=True, on_startup=on_startup)
