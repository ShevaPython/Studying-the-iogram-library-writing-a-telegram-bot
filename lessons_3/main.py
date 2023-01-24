# from aiogram import Bot, executor, types, Dispatcher
# import logging
# from config import TOKEN
#
# logging.basicConfig(level=logging.INFO)
# """
# Изучаем
# 1.on_startup -функция отображения в телеграм боте
# 2.parse_mod = "HTML" параметр сообщений
# 3.emoji,stickers -как отправлять емоджи и стикеры
# """
#
# bot = Bot(token=TOKEN)
# db = Dispatcher(bot)
#
#
# async def on_startup(_):
#     print("Я готов к работе,поехали!!")
#
#
# @db.message_handler(commands=["start"])
# async def start_command(message: types.Message):
#     await message.answer(text="<em>Добро пожаловать</em> в наш <b>Tелеграм бот!</b>", parse_mode="HTML")
#     await bot.send_sticker(message.from_user.id,
#                            sticker="CAACAgIAAxkBAAEHaYljz9B4xcmfIlXoU-VjwIM1v5sCRAACRgADUomRI_j-5eQK1QodLQQ")
#     await message.delete()
#
#
# @db.message_handler(commands=["give"])
# async def giv_emoji(message: types.Message):
#     await message.answer(text="Ну на!))")
#     await bot.send_sticker(message.from_user.id,
#                            sticker="CAACAgIAAxkBAAEHaYtjz9B6g-9Uk2x2TbHpAAEPy9OHBm8AAj4AA1KJkSOMfEPiTz8Lbi0E")
#     await message.delete()
#
# @db.message_handler()
# async def a_parrot(message:types.Message):
#     await message.reply(message.text + "❤️")
#
#
# if __name__ == "__main__":
#     executor.start_polling(db, skip_updates=True, on_startup=on_startup)
