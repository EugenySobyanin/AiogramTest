from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def get_main_menu(role: str):
    """Главное меню для всех ролей."""
    base_buttons = {
        "barista": ["/slots", "/my_slots", "/going"],
        "manager": [
            "/user_conf", "/creating_shifts", "/edit_shifts",
            "/change_booking", "/employement_conf", "/monitoring"
        ],
        "admin_extra": [
            "/create_cafe", "/edit_cafe", "/create_user", "/edit_user"
        ]
    }

    builder = ReplyKeyboardBuilder()

    if role == "barista":
        buttons = base_buttons["barista"]
    elif role == "manager":
        buttons = base_buttons["manager"]
    elif role == "admin":
        buttons = base_buttons["manager"] + base_buttons["admin_extra"]

    for button_text in buttons:
        builder.button(text=button_text)

    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def create_reply_keyboard(
    buttons: list[str],
    buttons_per_row: int = 2,
    resize_keyboard: bool = True,
    one_time_keyboard: bool = False,
    selective: bool = False,
) -> ReplyKeyboardMarkup:
    """
    Создает ReplyKeyboardMarkup из списка кнопок.

    Args:
        buttons: Список текстов для кнопок (например, ["Да", "Нет"])
        buttons_per_row: Количество кнопок в одном ряду (по умолчанию 2)
        resize_keyboard: Автоматически изменять размер клавиатуры (по умолчанию True)
        one_time_keyboard: Скрывать клавиатуру после использования (по умолчанию False)
        selective: Показывать клавиатуру только определенным пользователям (по умолчанию False)

    Returns:
        ReplyKeyboardMarkup: Готовая клавиатура для отправки в сообщении
    """
    builder = ReplyKeyboardBuilder()
    
    for button_text in buttons:
        builder.button(text=button_text)
    
    builder.adjust(buttons_per_row)
    
    return builder.as_markup(
        resize_keyboard=resize_keyboard,
        one_time_keyboard=one_time_keyboard,
        selective=selective,
    )