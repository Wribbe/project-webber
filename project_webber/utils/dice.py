from project_webber.utils.db import db_execute, db_commit

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
