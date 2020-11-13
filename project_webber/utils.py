import sqlite3
from pathlib import Path

from flask import g

HERE = Path(__file__).parent.resolve()
DATABASE = Path(HERE, 'project_webber.sqlite3')


def db_execute():
  pass


def db_commit():
  _db_get().commit()


def _db_con():
  return sqlite3.connect(str(DATABASE))


def _db_init():
  schema = Path(HERE, 'schema.sql')
  db = _db_con()
  db.cursor().executescript(schema.read_text())
  db.commit()


def _db_get():
  if not DATABASE.is_file():
    _db_init()
  if '_database' not in g:
    g._database = _db_con()
  return g._database
