#!/usr/bin/python3

#####=====----- VARIABLES -----=====#####
ROOT_INDEX_FILE = 'ADDS/index.html'


def server_root():
    with open(ROOT_INDEX_FILE, 'r', encoding='utf-8') as f_:
        output_ = f_.read()
    return output_


def register_post(user_dict: dict) -> dict:
    ''' Регистрация нового пользователя
    Arguments:
        user_dict [dict] -- Словарь (json) с обязательными ключами
            'phone', 'login', 'password', 'name', 'birth'
            и с необязательными ключами 'tg', 'email'
    Returns:
        output [dict] -- Словарь (json) с ключом идентификатора
            пользователя 'user_id', или с ключами 'code', 'text'
            в случае ошибки
    '''
    return user_dict


#####=====----- THE END -----=====#########################################