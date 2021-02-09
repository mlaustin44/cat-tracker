import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory=sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@click.command('init-db')
@with_appcontext
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    click.echo('Database initialized')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)

# class DB:
#     def __init__(self, db_file):
#         #check if the data exists
#         new_db = not os.path.exists(db_file)

#         self.conn = sqlite3.connect(db_file)

#         if new_db:
#             c = self.conn.cursor()
#             c.execute("""CREATE TABLE readings (
#                             id INTEGER PRIMARY KEY,
#                             source TEXT,
#                             ble_uuid TEXT,
#                             ble_name TEXT,
#                             timestamp INTEGER,
#                             ble_rssi INTEGER)""")
#             self.conn.commit()

#     def add_entry(self, source, ble_uuid, ble_name, timestamp, ble_rssi):
#         c = self.conn.cursor()
#         c.execute(f'INSERT INTO readings (source, ble_uuid, ble_name, timestamp, ble_rssi) VALUES ({source}, {ble_uuid}, {ble_name}, {timestamp}, {ble_rssi})')
#         self.conn.commit()