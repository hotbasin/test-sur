#!/usr/bin/python3

from bottle import HTTPError, get, post, request, run

import api_module as api_


#####=====----- BOTTLE DEFINITIONS -----=====#####
@get('/')
def server_root():
    return api_.server_root()


@post('/v1/auth/register')
def register_post():
    dict_ = request.body
    return api_.register_post(request.json)


@post('/v1/auth/login')
def login_post():
    return 'Login authenticated'


@get('/v1/user')
def user_get():
    user_id = request.query.id
    str_ = f'Your query is {user_id}'
    return str_


#####=====----- MAIN -----=====#####
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

#####=====----- THE END -----=====#########################################