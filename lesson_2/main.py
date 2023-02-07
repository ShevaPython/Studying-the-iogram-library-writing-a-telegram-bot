from aiogram import Bot, executor, Dispatcher, types
import logging
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
db = Dispatcher(bot)

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""


@db.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@db.message_handler(commands=["start"])
async def help_command(message: types.Message):
    await message.answer(text=F"Привет я твой персональный телеграм Бот!"
                              F"Приятно познакомиться ")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)
