import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()


TOKEN = getenv("BOT_TOKEN")
ADMINS = getenv('ADMINS').split(',')
PROVIDER_TOKEN = getenv('PROVIDER_TOKEN')
WEB_URL = getenv('WEB_URL')


dp = Dispatcher()


async def main() -> None:
    from bot.handlers import start_router, category_router

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(start_router, category_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
