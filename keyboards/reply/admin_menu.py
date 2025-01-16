from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

admin_menu = ReplyKeyboardBuilder(
    markup=[
        [
            KeyboardButton(text="📄 Maqola uchun sertifikat")  # Document emoji for certificates
        ]
    ]
).adjust(1, 1).as_markup(resize_keyboard=True, one_time_keyboard=False)
