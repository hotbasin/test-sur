#!/usr/bin/python3

from bottle import HTTPError, route, run


#####=====----- VARIABLES -----=====#####
ROOT_INDEX_FILE = 'index.html'


#####=====----- BOTTLE DEFINITIONS -----=====#####
@route('/')
def server_root():
    with open(ROOT_INDEX_FILE, 'r', encoding='utf-8') as f_:
        output_ = f_.read()
    return output_


#####=====----- MAIN -----=====#####
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

#####=====----- THE END -----=====#########################################