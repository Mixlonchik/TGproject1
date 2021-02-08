
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keybord_menu import menu
from main import dp
#
#
#
#
# @dp.message_handler(Command("menu"))
# async def show_menu(message: Message):
#     await message.answer("Выберите товар из меню ниже", reply_markup=menu)

def init(bot, dp):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply(f"Здарова, {message.from_user.full_name}!\nЯ - великий повторитель!\nPowered by aiogram.")


    @dp.message_handler(Command("menu"))
    async def show_menu(message: Message):
        await message.answer(
            f"Что {message.from_user.full_name} хочет делать дальше?",
            reply_markup=menu)


    @dp.message_handler(Text(equals=["Перейти к покупкам", "Настройки"]))
    async def get_button(message: Message):
        await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())
    #     ТУТ ДОЛЖНА БЫТЬ ССЫЛКА НА ИНЛАЙН КНОПКИ

    @dp.message_handler(Text(equals="Выбрать Язык"))
    async def choose_lang(message: Message):
        await message.answer(f"Пожалуйста, выберите язык, на котором Вам удобнее разговаривать",
                             reply_markup=ReplyKeyboardRemove())

    @dp.message_handler()
    async def echo(message: types.Message):
        # old style:
        # await bot.send_message(message.chat.id, message.text)

        await message.answer(message.text)