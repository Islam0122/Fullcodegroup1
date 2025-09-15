import asyncio
from aiogram import Bot,Dispatcher
from .islam_handlers import islam_router
from .nazima03_handlers import nazima03_router
from .aijarkyn_handlers import aijarkyn_router
from .aisara_handlers import aisara_router
from .Aibiike_handlers import Aibiike_router
from .yrys_handlers import yrys_router
TOKEN = "7427361367:AAGKMJ1hU9YnqY_hLtIPFNU4HclqcnReBl0gi"
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(nazima03_router)
dp.include_router(islam_router)
dp.include_router(aijarkyn_router)
dp.include_router(aisara_router)
dp.include_router(Aibiike_router)
dp.include_router(yrys_router)


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