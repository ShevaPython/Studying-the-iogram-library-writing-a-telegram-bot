from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_start_bot = KeyboardButton(text='Давай начнем 🤙')
button1 = KeyboardButton(text='Help 🆘')
button2 = KeyboardButton(text='random_photo 🎲')
button3 = KeyboardButton(text='jokes 😂')
button4 = KeyboardButton(text='giv_cat 😽')
button5 = KeyboardButton(text='description 👀')
kb.add(button_start_bot,button2, button3, button4).add(button1, button5)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
button_random = KeyboardButton(text='Рандом🎲')
button_menu = KeyboardButton(text='Меню⏪')
kb_photo.add(button_random, button_menu)

kb_joke = ReplyKeyboardMarkup(resize_keyboard=True)
button_menu = KeyboardButton(text='Меню⏪')
button_random_joke = KeyboardButton(text="Хочу анекдот 🫰")
kb_joke.add(button_random_joke,button_menu)