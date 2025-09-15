from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile


islam_router = Router()

@islam_router.message(F.text == "/islam_start")
async def start(message: Message):
    await message.answer(
        "hello my name is islam"
        "i am teacher"
    )

