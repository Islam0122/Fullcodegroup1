from aiogram import Router, F , Bot
from aiogram.types import Message, CallbackQuery, FSInputFile


aijarkyn_router = Router()

@aijarkyn_router.message(F.text == "/aijarkyn_start")
async def start(message: Message):
    await message.answer(
        "hello my name is aijarkyn"
        "i am teacher"
    )
