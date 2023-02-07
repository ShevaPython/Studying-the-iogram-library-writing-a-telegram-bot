from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

ilkm = InlineKeyboardMarkup(row_width=3)
ibGit = InlineKeyboardButton(text="GIT",
                             url="https://github.com/ShevaPython")
ibTelegram = InlineKeyboardButton(text="Telegram",
                                  url="https://t.me/Sergey_ShevaA")
ibInstagram = InlineKeyboardButton(text="Instagram",
                                   url="https://www.instagram.com/shevtsovsn/?igshid=MDM4ZDc5MmU%3D")
ilkm.add(ibInstagram).add(ibGit).add(ibTelegram)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b = KeyboardButton(text='/link')
kb.add(b)
