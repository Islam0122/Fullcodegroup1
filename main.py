import asyncio
from aiogram import Bot,Dispatcher
from .nazima03_handlers import nazima03_router

TOKEN = "7427361367:AAGKMJ1hU9YnqY_hLtIPFNU4HclqcnReBl0gi"
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(nazima03_router)


async def startup():
    print("----------------------- i woke up BOSS ---------------------------")

async def off():
    print(" ----------------------i asleep BOSS -----------------------------")

async def main():
    dp.startup.register(startup)
    dp.shutdown.register(off)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())