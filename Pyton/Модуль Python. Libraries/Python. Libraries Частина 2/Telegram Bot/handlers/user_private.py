from aiogram.filters import CommandStart, Command
from aiogram import types, Router
import random

user_private_router = Router()

@user_private_router.massage(CommandStart())
async def star_cmd(message: types.Message):
    await message.answer(f"Hello my dear frend{message.from_user.full_name}")

# @user_private_router.message(Command('menu'))
# async def menu_cmd(message: types.Message):
#     await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_markup.add(
        types.KeyboardButton('/menu'),
        types.KeyboardButton('/help'),
        types.KeyboardButton('/echo'),
        types.KeyboardButton('/start')
    )

    await message.answer("Menu:", reply_markup=keyboard_markup)

@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Help: How can i help you&")

@user_private_router.message(Command('echo'))
async def echo_cmd(message: types.Message):
    await message.answer("Echo: Send me a message, and I'll repeat it.")

@user_private_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer("Welcome! This is the start message.")

@user_private_router.message()
async def echo(message: types.Message):
    hello = random.choise(['hi', 'hello', 'привіт', "здоровенькі були"])
    byebye = random.choise(['goodbuy', 'buy', 'бувай', "пака"])
    text = message.text
    if text in ['hi', 'hello', 'привіт', "здоровенькі були"]:
        await message.answer(f"Hello {message.from_user.full_name}")
    elif text in ['goodbuy', 'buy', 'бувай', "пака"]:
        await message.answer(f"Goodbye {message.from_user.full_name}")
    else:
        await message.reply("I don't understand you")
#   await message.answer("message.text")
#   await message.reply(f"Hello my dear frend")