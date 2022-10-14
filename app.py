from bottle import run, route
import sqlite3

@route('/')
def index():
    #Home Page to navigate the website
    print("On the home web page")
    html =  """<h1>Home Page</h1>'
            <a href='/SQL/Easy'>Easy SQL Inejction </a>"""
    # Give options for the user to navigate to new pages
    return html 

@route('/SQL/<id>')
def SQLEasy(id):
    print("On SQL Injection Page level " + id)
    html =  """<h1>Viewing the SQL Injection """+ id +""" Page </h1> 
            <a href='/'>Go to Home Page </a>"""
    #Return to the home page
    return html

# Old code when learning about routes
#@route('/login')
#def login():
#    return '<h1>Viewing Login Page<h1>'

if __name__ == '__main__':
    run(debug=True, reloader=True)