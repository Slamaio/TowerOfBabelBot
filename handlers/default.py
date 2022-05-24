from aiogram import types


async def start(message: types.Message):
    await message.reply("/help to show this message\n"
                        + "!t <text> -- translate to english\n"
                        + "!t-<lang_code> <text> -- translate to chosen language\n"
                        + "!g <text> -- identify the language\n"
                        + "!c <lang_name> -- get the lang_code by languane name")
