from aiogram import types
from googletrans import Translator

from config import *


translator = Translator()

def get_dest(message: types.Message) -> str:
    dest = message.text.split(' ', 1)
    dest = dest[0].split('-', 1)
    return dest[1]

def get_text(message: types.Message) -> str:
    text = message.text.split(' ', 1)
    return text[1]

def is_default(message: types.Message) -> bool:
    is_default = message.text.split(' ', 1)[0] == PREFIX+TRANS_COMMANDS[0]
    return is_default

async def translate(message: types.Message):
    text = get_text(message)
    dest = 'en' if is_default(message) else get_dest(message)
    tr_message = translator.translate(text, dest)
    await message.reply(tr_message.text)
