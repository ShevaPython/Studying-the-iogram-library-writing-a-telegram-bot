#
# import logging
#
# from aiogram import Bot, Dispatcher, executor, types
#
# import config
# from config import TOKEN
#
#
# API_TOKEN = TOKEN
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

#
# @dp.message_handler()
# async def echo(message: types.Message):
#
#     await message.reply(text=message.text)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
