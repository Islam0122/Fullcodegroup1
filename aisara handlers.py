from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile


aisara_router = Router()

@aisara_router.message(F.text == "/aisara_start")
async def start(message: Message):
    await message.answer(
        "Hello my name is Aisara!"
        "I am an english interpreter."
    )