# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Response
import createdb
import controller

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'yhack.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('YHACK_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    return db

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db = init_db()
    createdb.addData(db)
    print 'Initialized the database.'

@app.route('/')
def show_entries():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    return render_template('show_entries.html')

@app.route('/eventsearch/<jsdata>', methods=['GET', 'POST'])
def searchEvents(jsdata):
	db = get_db()
	js = controller.findMatches(jsdata, db)
	resp = Response(js, status=200, mimetype='application/json')
	return resp
	# return controller.findMatches(jsdata, db)

@app.route('/booking/<jsdata>', methods=['GET', 'POST'])
def confirmBooking(jsdata):
	db = get_db()
	js = controller.addBooking(jsdata, db)
	resp = Response(js, status=200, mimetype='application/json')
	return resp