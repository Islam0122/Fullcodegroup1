from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile


nazima03_router = Router()

@nazima03_router.message(F.text == "/nazima03_start")
async def start(message: Message):
    await message.answer(
        "hello my name is nazima"
        "i am student"
    )
