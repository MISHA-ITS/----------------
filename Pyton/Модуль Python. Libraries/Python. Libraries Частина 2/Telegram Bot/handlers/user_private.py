from aiogram.filters import CommandStart, Command
from aiogram import types, Router
import random

user_private_router = Router()

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start")

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hello my dear friend {message.from_user.full_name}. I`m your personal telegram-bot!")
    
@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("How can i help you?")

@user_private_router.message(Command('echo'))
async def echo_cmd(message: types.Message):
    await message.answer("Send me a message, and I'll repeat it.")

@user_private_router.message()
async def feedback(message: types.Message):
    hello = random.choice(['hi', 'hello', 'привіт', "здоровенькі були"])
    byebye = random.choice(['goodbuy', 'buy', 'бувай', "пака"])
    text = message.text
    if text in ['hi', 'hello', 'привіт', "здоровенькі були"]:
        await message.answer(f"Hello {message.from_user.full_name}")
    elif text in ['goodbuy', 'buy', 'бувай', "пака"]:
        await message.answer(f"Goodbye {message.from_user.full_name}")
    else:
        await message.answer(message.text)