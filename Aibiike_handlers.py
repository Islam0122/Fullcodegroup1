from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile


Aibiike_router = Router()

@Aibiike_router.message(F.text == "/Aibiike_start")
async def start(message: Message):
    await message.answer(
        "hello my name is Aibiike"
        "i'm an IT specialist"
    )
