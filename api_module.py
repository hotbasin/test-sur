#!/usr/bin/python3

import uuid


def register_post(userdata_: dict) -> dict:
    ''' Первый метод API из ТЗ (Регистрация нового пользователя)
    Arguments:
        userdata_ [dict] -- Словарь/json с обязательными ключами
            'phone', 'login', 'password', 'name', 'birth'
            и с необязательными ключами 'tg', 'email'
    Returns:
        output_ [dict] -- Словарь/json с ключом идентификатора
            пользователя 'user_id', или с ключами 'code', 'text'
            в случае ошибки
    '''
    output_ = userdata_
    return output_

def tmp_register_post(userdata_):
    ''' Тестовый метод API для контроля из HTML
    '''
    output_ = userdata_
    return output_

def user_get(uid_: str) -> dict:
    ''' Третий метод API из ТЗ
    Arguments:
        uid_ [str] -- UID пользователя
    Returns:
        output_ [dict] -- Словарь/json со всеми ключами пользователя
            кроме 'password' или с ключами 'code', 'text'
            в случае ошибки
    '''
    output_ = f'Your query is {uid_}'
    return output_


#####=====----- THE END -----=====#########################################