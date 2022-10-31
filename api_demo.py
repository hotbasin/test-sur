#!/usr/bin/python3

from bottle import HTTPError, get, post, request, run

import api_module as api_


#####=====----- VARIABLES -----=====#####
ROOT_INDEX_FILE = 'ADDS/index.html'


#####=====----- BOTTLE DEFINITIONS -----=====#####
@get('/')
def server_root() -> str:
    ''' Аналог ServerRoot для проверки работоспособности Bottle
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX_FILE
    '''
    with open(ROOT_INDEX_FILE, 'r', encoding='utf-8') as f_:
        output_ = f_.read()
    return output_

@post('/v1/auth/register')
def register_post():
    return api_.register_post(request.json)

@post('/v1/auth/login')
def login_post():
    return 'Login authenticated'

@get('/v1/user')
def user_get():
    uid_ = request.query.id
    return api_.user_get(uid_)


#####=====----- TEMPORAL tests in browser -----=====#####
@post('/v2/auth/register')
def tmp_register_post():
    return api_.tmp_register_post(request.body)

@post('/v2/auth/login')
def tmp_login_post():
    return 'Login authenticated'


#####=====----- MAIN -----=====#####
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

#####=====----- THE END -----=====#########################################