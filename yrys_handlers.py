from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile


yrys_router = Router()

@yrys_router.message(F.text == "/yrys_start")
async def start(message: Message):
    await message.answer(
        "hello my name is yrys"
        "i am bot"
    )
