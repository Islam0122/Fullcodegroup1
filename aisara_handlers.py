from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile

from words import about_me_text
from aisara_keyboards import *

aisara_router = Router()

@aisara_router.message(F.text == "/aisara_start")
async def start(message: Message):
    await message.answer_photo(
        photo=FSInputFile("img.png"),
        caption=about_me_text,
        reply_markup=instagram_keyboard
    )