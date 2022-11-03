#!/usr/bin/python3

from bottle import HTTPError, get, post, request, run

import api_module as api_


''' =====----- Global variables -----===== '''
ROOT_INDEX_FILE = 'ADDS/index.html'


''' =====----- Bottle resources -----===== '''
@get('/')
def server_root() -> str:
    ''' Аналог ServerRoot для проверки работоспособности Bottle
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX_FILE
    '''
    with open(ROOT_INDEX_FILE, 'r', encoding='utf-8') as f_:
        return f_.read()

@post('/v1/auth/register')
def register_post():
    ''' Первый метод API из ТЗ
    '''
    return api_.register_post(request.json)

@post('/v1/auth/login')
def login_post():
    ''' Второй метод API из ТЗ
    '''
    return api_.login_post(request.json)

@get('/v1/user')
def user_get():
    ''' Третий метод API из ТЗ
    '''
    uid_ = request.query.id
    return api_.user_get(uid_)


''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

#####=====----- THE END -----=====#########################################