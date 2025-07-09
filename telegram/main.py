import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings import BOT_TOKEN, WEB_APP_URL

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="📷 Сканировать QR/Штрих-код", web_app=WebAppInfo(url=WEB_APP_URL)
        )
    )
    await message.answer(
        "Нажми кнопку ниже, чтобы открыть сканер QR/штрих-кодов:",
        reply_markup=builder.as_markup(),
    )


@dp.message()
async def handle_webapp_data(message: types.Message):
    if message.web_app_data:
        await message.answer(
            f"📦 Сканировано:\n<code>{message.web_app_data.data}</code>"
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
