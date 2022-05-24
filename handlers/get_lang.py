from aiogram import types
from googletrans import Translator

from config import *


translator = Translator()

async def get_lang(message: types.Message):
    lang = translator.detect(message.text.split(' ', 1)[1]).lang
    lang = LANGUAGES[lang]
    await message.reply(lang)