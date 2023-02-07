from aiogram import Bot, Dispatcher, executor, types
from keyboard import kb, ikb
from config import TOKEN
import logging

"""
CallbackQuery

- Класс возвращает обьект запроса обратного в ответ на некоторое событие
- Имеет множество атрибутов id :str
                            from: user
                            message :Message()
                            data : str
- callback:types.CallbackQuery - экземпляр класса CallbackQuery хранит в себе данные сгенерированного запроса ,
  обрабатываеться посредством обьекта callback_query_handler

- callback_query_handler - декоратор использующийся для реализации обработки обьекта запроса,может как правило обрабатывать
  не 1 а множество обьектов callbackquery.для избирательной обработки используеться специальный фильтр!
"""

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
db = Dispatcher(bot)


async def on_start_up(_):
    print("I am ready")


@db.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать я Ваш персональный Бот",
                           reply_markup=kb)


@db.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://cdn.pixabay.com/photo/2023/01/27/01/40/brothers-7747561_960_720.jpg',
                         caption='Тебе нравиться это фото??',
                         reply_markup=ikb)


@db.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        return await callback.answer(text="Она мне тоже понравилась))")
    elif callback.data == 'dislike':
        await callback.answer(text="Ну да,полное г...о")
    else:
        await callback.answer(text='Согласен такое себе)')


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True, on_startup=on_start_up)
