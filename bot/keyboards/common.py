from typing import Optional

from aiogram.utils.keyboard import (InlineKeyboardMarkup,
                                    InlineKeyboardBuilder,
                                    ReplyKeyboardBuilder,
                                    ReplyKeyboardMarkup)

from keyboards.constant import (BASE_BUTTONS, BUTTONS_IN_ROW)


def create_reply_keyboard(
    buttons: list[str],
    buttons_per_row: int = BUTTONS_IN_ROW.get('default', 2),
    resize_keyboard: bool = True,
    one_time_keyboard: bool = False,
) -> ReplyKeyboardMarkup:
    """
    Универсальная Reply клавиатура.

    Args:
        buttons: Список текстов для кнопок
        buttons_per_row: Количество кнопок в ряду
        resize_keyboard: Автоматическое изменение размера
        one_time_keyboard: Скрывать после использования

    Returns:
        Готовая клавиатура
    """
    builder = ReplyKeyboardBuilder()
    for button_text in buttons:
        builder.button(text=button_text)
    builder.adjust(buttons_per_row)
    return builder.as_markup(
        resize_keyboard=resize_keyboard,
        one_time_keyboard=one_time_keyboard,
    )


def create_inline_keyboard(
    buttons: list[dict[str, str]],
    buttons_per_row: int = 2
) -> InlineKeyboardMarkup:
    """
    Универсальная Inline клавиатура.
    Каждая кнопка задаётся словарём: {"text": "Текст", "callback_data": "data"}
    """
    builder = InlineKeyboardBuilder()
    for button in buttons:
        builder.button(text=button["text"],
                       callback_data=button["callback_data"])
    builder.adjust(buttons_per_row)
    return builder.as_markup()


def get_main_menu(role: Optional[str] = None) -> ReplyKeyboardMarkup:
    """
    Главное меню с учётом роли.
    """
    buttons = BASE_BUTTONS.get(role)
    return create_reply_keyboard(
        buttons,
        buttons_per_row=BUTTONS_IN_ROW.get('main_menu', 2)
    )
