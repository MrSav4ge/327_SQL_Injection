from bottle import run, route

@route('/')
def index():
    return '<h1>Hello World</h1>'

@route('/login')
def login():
    return '<h1>Viewing Login Page<h1>'

@route('/SQL/<id>')
def SQLEasy(id):
    return '<h1>Viewing the SQL Injection ' + id + ' Page </h1>'



if __name__ == '__main__':
    run(debug=True, reloader=True)