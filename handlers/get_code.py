from aiogram import types
from googletrans import Translator
from googletrans.constants import LANGCODES

from config import *


translator = Translator()

async def get_code(message: types.Message):
    code = LANGCODES[message.text.split(' ', 1)[1].lower()]
    await message.reply(code)