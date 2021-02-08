import logging

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import Command, Text
# from aiogram.types import Message, ReplyKeyboardRemove
#
# from keybord_menu import menu
# _________________________________________________________


API_TOKEN = '1138058936:AAHPrXC5ZIzzoH5zx18PKbPejfSubjhazBA' # пойдет в config.py


# Configure logging________________________________________
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)                  # loader.py
dp = Dispatcher(bot)                         # loader.py    


# HANDLERS__________________________________________________

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply(f"Здарова, {message.from_user.full_name}!\nЯ - великий повторитель!\nPowered by aiogram.")
#
#
# @dp.message_handler(Command("menu"))
# async def show_menu(message: Message):
#     await message.answer(f"Что {message.from_user.full_name} хочет делать дальше?", reply_markup=menu)
#
# @dp.message_handler(Text(equals=["Перейти к покупкам", "Выбрать Язык", "Настройки"]))
# async def get_button(message: Message):
#     await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)

def run():
  from handlers_menu import init
  init(bot, dp)
# RUN________________________________________________________

if __name__ == '__main__':
    run()
    executor.start_polling(dp, skip_updates=True)
