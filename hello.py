from bottle import route, run, get, post, request # or route

@route('/hello')
def hello():
    return "<h1>Hello World!<h1>"
    
@get('/app')
def app():
    return '''
        <form action="/app" method="post">
            Input: <input name="myRequest" type="text" />
        </form>
    '''

@post('/app')
def reply():
    myRequest = request.forms.get('myRequest')
    return app()+"request got: "+myRequest

run(host='127.0.0.1',port=8081)
