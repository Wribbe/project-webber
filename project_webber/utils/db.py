import sqlite3
from pathlib import Path

from flask import g

HERE = Path(__file__).parent.resolve()
DATABASE = Path(HERE.parent, 'project_webber.sqlite3')


def db_execute(command, args=(), cursor=None):
  if type(args) not in [list, tuple]:
    args = (args,)
  if not cursor:
    cursor = _db_get().cursor()
  return cursor.execute(command, args)


def db_query(query, args=(), one=True):
  cursor = db_execute(query, args)
  results = cursor.fetchone() if one else cursor.fetchall()
  cursor.close()
  return results if results else []


def db_commit():
  _db_get().commit()


def _db_con():
  return sqlite3.connect(str(DATABASE))


def _db_init():
  schema = Path(HERE, 'schema.sql')
  db = _db_con()
  cursor = db.cursor()
  cursor.executescript(schema.read_text())
  db.commit()
  cursor.close()


def _db_get():
  if not DATABASE.is_file():
    _db_init()
  if '_database' not in g:
    g._database = _db_con()
    g._database.row_factory = sqlite3.Row
  return g._database
