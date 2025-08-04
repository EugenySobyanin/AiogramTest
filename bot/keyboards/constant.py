# Константы для ролей
ROLE_BARISTA = 'barista'
ROLE_MANAGER = 'manager'
ROLE_ADMIN = 'admin'

# Константы для команд
CMD_START = '/start'
CMD_SLOTS = '/slots'
CMD_MY_SLOTS = '/my_slots'
CMD_GOING = '/going'
CMD_USER_CONF = '/user_conf'
CMD_CREATING_SHIFTS = '/creating_shifts'
CMD_EDIT_SHIFTS = '/edit_shifts'
CMD_CHANGE_BOOKING = '/change_booking'
CMD_EMPLOYEMENT_CONF = '/employement_conf'
CMD_MONITORING = '/monitoring'
CMD_CREATE_CAFE = '/create_cafe'
CMD_EDIT_CAFE = '/edit_cafe'
CMD_CREATE_USER = '/create_user'
CMD_EDIT_USER = '/edit_user'

# Базовые кнопки для каждой роли
BARISTA_BUTTONS = [CMD_SLOTS, CMD_MY_SLOTS, CMD_GOING]
MANAGER_BUTTONS = [
        CMD_USER_CONF, CMD_CREATING_SHIFTS, CMD_EDIT_SHIFTS,
        CMD_CHANGE_BOOKING, CMD_EMPLOYEMENT_CONF, CMD_MONITORING
]
ADMIN_BUTTONS = MANAGER_BUTTONS + [
        CMD_CREATE_CAFE, CMD_EDIT_CAFE, CMD_CREATE_USER, CMD_EDIT_USER
]
GUEST_BUTTONS = [CMD_START]

BASE_BUTTONS = {
    ROLE_BARISTA: BARISTA_BUTTONS,
    ROLE_MANAGER: MANAGER_BUTTONS,
    ROLE_ADMIN: ADMIN_BUTTONS,
}

# Количество кнопок для разных меню
BUTTONS_IN_ROW = {
    'default': 2,
    'main_menu': 2,

}
