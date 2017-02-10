from bottle import route, run

@route('/hello')
def hello():
    return "<h1>Hello World!<h1>"

run(host='127.0.1.1',port=8080)
