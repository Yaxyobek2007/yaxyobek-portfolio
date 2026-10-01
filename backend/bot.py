import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from dotenv import load_dotenv


# =========================
# 1. .env faylini o‘qish
# =========================

env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env faylida topilmadi!")


# =========================
# 2. Bot va Dispatcher
# =========================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# =========================
# 3. Asosiy menyu
# =========================

def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👤 About Me",
                    callback_data="about"
                ),
                InlineKeyboardButton(
                    text="🚀 Projects",
                    callback_data="projects"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💼 Experience",
                    callback_data="experience"
                ),
                InlineKeyboardButton(
                    text="🏆 Achievements",
                    callback_data="achievements"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🛠 Skills",
                    callback_data="skills"
                ),
                InlineKeyboardButton(
                    text="🎓 Education",
                    callback_data="education"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📜 Certificates",
                    callback_data="certificates"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="👔 Recruiter View",
                    callback_data="recruiter"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📄 Resume",
                    callback_data="resume"
                ),
                InlineKeyboardButton(
                    text="📩 Contact",
                    callback_data="contact"
                ),
            ],
        ]
    )


# =========================
# 4. /start
# =========================

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "YAXYOBEK NEMATILLAEV\n\n"
        "Professional Portfolio\n\n"
        "Explore my projects, experience, "
        "achievements and professional journey.",
        reply_markup=main_menu(),
    )


# =========================
# 5. Tugmalar
# =========================

@dp.callback_query(F.data == "about")
async def about_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "👤 ABOUT ME\n\n"
        "Bu bo‘limda Yaxyobek haqida professional "
        "ma’lumotlar bo‘ladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "projects")
async def projects_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🚀 PROJECTS\n\n"
        "Bu yerda barcha professional loyihalar "
        "case study formatida chiqadi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "experience")
async def experience_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "💼 EXPERIENCE\n\n"
        "Bu yerda ish tajribasi va professional faoliyat "
        "timeline ko‘rinishida bo‘ladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "achievements")
async def achievements_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🏆 ACHIEVEMENTS\n\n"
        "Bu yerda yutuqlar, mukofotlar va milestone'lar "
        "ko‘rsatiladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "skills")
async def skills_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🛠 SKILLS\n\n"
        "Bu yerda texnologiyalar va professional "
        "ko‘nikmalar bo‘ladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "education")
async def education_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎓 EDUCATION\n\n"
        "Bu yerda ta’lim, kurslar va o‘qish jarayoni "
        "haqidagi ma’lumotlar bo‘ladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "certificates")
async def certificates_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "📜 CERTIFICATES\n\n"
        "Bu yerda sertifikatlar va ularning "
        "verification linklari bo‘ladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "recruiter")
async def recruiter_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "👔 RECRUITER VIEW\n\n"
        "HR va kompaniya vakillari uchun "
        "eng muhim professional ma’lumotlar "
        "bitta joyda ko‘rsatiladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "resume")
async def resume_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "📄 RESUME\n\n"
        "Bu yerda professional CV va PDF Resume "
        "joylashtiriladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


@dp.callback_query(F.data == "contact")
async def contact_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "📩 CONTACT\n\n"
        "Bu yerda Telegram, Email, LinkedIn va "
        "boshqa professional kontaktlar bo‘ladi.",
        reply_markup=back_button(),
    )
    await callback.answer()


# =========================
# 6. Orqaga qaytish
# =========================

def back_button() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="← Back to Portfolio",
                    callback_data="home"
                )
            ]
        ]
    )


@dp.callback_query(F.data == "home")
async def home_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "YAXYOBEK NEMATILLAEV\n\n"
        "Professional Portfolio\n\n"
        "Explore my projects, experience, "
        "achievements and professional journey.",
        reply_markup=main_menu(),
    )
    await callback.answer()


# =========================
# 7. Botni ishga tushirish
# =========================

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())