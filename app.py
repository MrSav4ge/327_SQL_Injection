from unittest import result
from urllib.error import HTTPError
import bottle
import bottle.ext.sqlite



app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='Users.db')
app.install(plugin)


@app.route('/')
def index():
    #Home Page to navigate the website
    print("On the home web page")
    html =  """<h1>Home Page</h1>
            <a href='/SQL/Easy'>Easy SQL Inejction </a>"""
    # Give options for the user to navigate to new pages
    return html 

@app.route('/SQL/<id>')
def SQLEasy(id):
    print("On SQL Injection Page level " + id)
    html =  """<h1>Viewing the SQL Injection """+ id +""" Page </h1> 
            <a href='/'>Go to Home Page </a>"""
    #Return to the home page
    return html

@app.route('/DBview')
def DBview(db):
    username = "Alex"
    sql_statement = "SELECT * FROM Users WHERE User = '{username}'"
    user = db.execute(sql_statement.format(username=username)).fetchone()
    if(user):
        name = user[0]
        print("successfully pulled from database")
        return "<h1> " + name + " </h1>"
    return "<h1> Error </h1>"

    

# Old code when learning about routes
#@app.route('/login')
#def login():
#    return '<h1>Viewing Login Page<h1>'

if __name__ == '__main__':
    app.run(debug=True, reloader=True)