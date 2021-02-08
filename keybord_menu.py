from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Перейти к покупкам"),
        ],
        [
            KeyboardButton(text="Выбрать Язык"),
            KeyboardButton(text="Настройки")
        ],
    ],
    resize_keyboard=True
)