#!/usr/bin/python3

import json
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Session

import api_validations as v_

#####=====----- Variables -----=====#####
DB_PATH = 'sqlite:///sqlite/db.sqlite'
# Base = sa.ext.declarative.declarative_base()
Base = declarative_base()


#####=====----- Classes -----=====#####
class User(Base):
    __tablename__ = 'Users'
    uid = sa.Column(sa.String(36), primary_key=True)
    name = sa.Column(sa.String(1024))
    birth = sa.Column(sa.String(10))
    login = sa.Column(sa.String(1024))
    password = sa.Column(sa.String(1024))
    phone = sa.Column(sa.String(12))
    email = sa.Column(sa.String(1024))
    tg = sa.Column(sa.String(1024))

class Error(Base):
    __tablename__ = 'Errors'
    code = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.Text(1024))

#####=====----- API methods -----=====#####
def register_post(userdata_: dict) -> dict:
    ''' Первый метод API из ТЗ (Регистрация нового пользователя)
    Arguments:
        userdata_ [dict] -- Словарь/json с обязательными ключами
            'name', 'birth', 'login', 'password', 'phone'
            и с необязательными ключами 'email', 'tg'
    Returns:
        [dict] -- Словарь/json с ключом идентификатора пользователя
            'uid', или с ключами 'code', 'text' в случае ошибки
    '''
    error_code = v_.validate_all(userdata_)
    if error_code == 0:
        uid_ = str(uuid.uuid4())
        name_ = userdata_['name']
        birth_ = userdata_['birth']
        login_ = userdata_['login']
        password_ = userdata_['password']
        phone_ = userdata_['phone']
        email_ = userdata_.get('email')
        tg_ = userdata_.get('tg')
        new_user = User(
            uid=uid_,
            name=name_,
            birth=birth_,
            login=login_,
            password=password_,
            phone=phone_,
            email=email_,
            tg=tg_
        )
        engine = sa.create_engine(DB_PATH)
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
        output_ = {'uid': uid_}
    else:
        pass
    return json.dumps(output_, indent=4)

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