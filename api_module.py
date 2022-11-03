#!/usr/bin/python3

import json
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Session

import api_validations as v_

#####=====----- Variables -----=====#####
DB_PATH = 'sqlite:///sqlite/db.sqlite3'
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
    err_code = v_.validate_all(userdata_)
    engine = sa.create_engine(DB_PATH)
    if err_code == 0:
        uid_ = str(uuid.uuid4())
        name_ = userdata_.get('name')
        birth_ = userdata_.get('birth')
        login_ = userdata_.get('login')
        password_ = userdata_.get('password')
        phone_ = userdata_.get('phone')
        email_ = userdata_.get('email')
        tg_ = userdata_.get('tg')

        new_user = User(uid=uid_,
                        name=name_,
                        birth=birth_,
                        login=login_,
                        password=password_,
                        phone=phone_,
                        email=email_,
                        tg=tg_
                       )
        with Session(engine) as add_session:
            add_session.add(new_user)
            add_session.commit()
        output_ = dict(uid=uid_)
    else:
        with Session(engine) as err_session:
            error_ = err_session.query(Error).filter(Error.code == err_code)[0]
            output_ = dict(code=error_.code, text=error_.text)
    return json.dumps(output_, indent=4)


def login_post(credentials_: dict) -> dict:
    ''' Второй метод API из ТЗ (Авторизация)
    Arguments:
        credentials_ [dict] -- Словарь/json с ключами 'login',
            'password'
    Returns:
        [dict] -- Словарь/json с ключом идентификатора пользователя
            'uid', или с ключами 'code', 'text' в случае ошибки
    '''
    login_ = credentials_.get('login')
    password_ = credentials_.get('password')
    engine = sa.create_engine(DB_PATH)
    with Session(engine) as auth_session:
        try:
            user_ = auth_session.query(User).filter(User.login == login_)[0]
            if user_.password == password_:
                output_ = dict(uid=user_.uid)
            else:
                error_ = auth_session.query(Error).filter(Error.code == 800)[0]
                output_ = dict(code=error_.code, text=error_.text)
        except:
            error_ = auth_session.query(Error).filter(Error.code == 800)[0]
            output_ = dict(code=error_.code, text=error_.text)
    return json.dumps(output_, indent=4)


def user_get(uid_: str) -> dict:
    ''' Третий метод API из ТЗ (Ответ на запрос id)
    Arguments:
        uid_ [str] -- UID пользователя
    Returns:
        [dict] -- Словарь/json со всеми ключами пользователя кроме
            'password' или с ключами 'code', 'text' в случае ошибки
    '''
    engine = sa.create_engine(DB_PATH)
    with Session(engine) as q_session:
        try:
            user_ = q_session.query(User).filter(User.uid == uid_)[0]
            output_ = dict(name=user_.name,
                           birth=user_.birth,
                           login=user_.login,
                           phone=user_.phone,
                           email=user_.email,
                           tg=user_.tg
                          )
        except:
            error_ = q_session.query(Error).filter(Error.code == 900)[0]
            output_ = dict(code=error_.code, text=error_.text)
    return json.dumps(output_, indent=4)

#####=====----- THE END -----=====#########################################