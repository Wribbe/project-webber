import sqlite3
from pathlib import Path

from flask import g

HERE = Path(__file__).parent.resolve()
DATABASE = Path(HERE, 'project_webber.sqlite3')


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
  return g._database


def dice_create(sides, paths=[], description=""):

  # Create the dice.
  cursor = db_execute(
    'INSERT INTO dice (description) VALUES (?)', description
  )
  id_dice = cursor.lastrowid

  # Create the sides.
  if not paths:
    paths = [""]*len(sides)
  id_sides = []
  for side, path in zip(sides, paths):
    db_execute(
      'INSERT INTO dice_side (value, path_graphic) VALUES (?,?)',
      (side, path),
      cursor=cursor,
    )
    id_sides.append(cursor.lastrowid)

  # Link the dice with the sides.
  for id_side in id_sides:
    db_execute(
      'INSERT INTO dice_side_link (id_dice, id_side) VALUES (?,?)',
      (id_dice, id_side),
      cursor=cursor
    )

  # Close the cursor and commit the changes.
  cursor.close()
  db_commit()
  return id_dice
