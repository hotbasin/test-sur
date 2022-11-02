#!/usr/bin/python3

def is_valid_name(name_: str) -> int:
    ''' Проверка имени пользователя.
        Проверяется только наличие и длина строки
    Arguments:
        name_ [str] -- Поле 'name'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if 0 < len(name_) <= 1024:
        return 0
    else:
        return 100

def is_valid_birth(birth_: str) -> int:
    ''' Проверка даты рождения
    Arguments:
        birth_ [str] -- Поле 'birth'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if len(birth_) == 10:
        # TO DO: проверка на совершеннолетие
        # return 210 при нарушении
        pass
        return 0
    else:
        return 200

def is_valid_login(login_: str) -> int:
    ''' Проверка логина пользователя
        Проверяется только наличие и длина строки
    Arguments:
        login_ [str] -- Поле 'login'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if 0 < len(login_) <= 1024:
        return 0
    else:
        return 300

def is_valid_password(password_: str) -> int:
    ''' Проверка пароля пользователя
        Проверяется только наличие и длина строки
    Arguments:
        password_ [str] -- Поле 'password'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if 0 < len(password_) <= 1024:
        return 0
    else:
        return 400

def is_valid_phone(phone_: str) -> int:
    ''' Проверка номера телефона пользователя
        Проверяется только наличие и длина строки
    Arguments:
        phone_ [str] -- Поле 'phone'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if len(phone_) == 12:
        return 0
    else:
        return 500

def is_valid_email(email_: str) -> int:
    ''' Проверка необязательного Email-адреса пользователя
        Может быть 'None', но если есть, проверяется только длина строки
    Arguments:
        email_ [str] -- Поле 'email'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if email_ is None or len(email_) <= 1024:
        return 0
    else:
        return 600

def is_valid_tg(tg_: str) -> int:
    ''' Проверка необязательного Telegram-логина пользователя
        Может быть 'None', но если есть, проверяется только длина строки
    Arguments:
        email_ [str] -- Поле 'email'
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код ошибки по таблице Errors
    '''
    if tg_ is None or len(tg_) <= 1024:
        return 0
    else:
        return 700


def validate_all(userdata_: dict) -> int:
    ''' Основная функция валидации входных данных.
        Последовательно проверяет все поля. При первой же ошибке
        возвращает код и прекращает валидацию.
    Arguments:
        userdata_ [dict] -- Словарь/json с данными пользователя
    Returns:
        [int] -- '0' при отсутствии ошибок,
            или код первой обнаруженной ошибки по таблице Errors
    '''
    code_list = [
        is_valid_name(userdata_.get('name')),
        is_valid_birth(userdata_.get('birth')),
        is_valid_login(userdata_.get('login')),
        is_valid_password(userdata_.get('password')),
        is_valid_phone(userdata_.get('phone')),
        is_valid_email(userdata_.get('email')),
        is_valid_tg(userdata_.get('tg')),
    ]
    for code_ in code_list:
        if code_ != 0:
            return code_
    return 0

#####=====----- THE END -----=====#########################################