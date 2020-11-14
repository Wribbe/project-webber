CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,email STRING NOT NULL
  ,name STRING NOT NULL
  ,secret STRING NOT NULL
);


CREATE TABLE roll (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,id_dice INTEGER NOT NULL
  ,id_user INTEGER NOT NULL
  ,id_result INTEGER NOT NULL
  ,FOREIGN KEY(id_user) REFERENCES user(id)
  ,FOREIGN KEY(id_dice) REFERENCES dice(id)
  ,FOREIGN KEY(id_result) REFERENCES dice_side(id)
);


CREATE TABLE dice (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,description STRING
);


CREATE TABLE dice_side (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,path_graphic STRING
  ,value STRING
);


CREATE TABLE dice_side_link (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  ,id_dice INTEGER NOT NULL
  ,id_side INTEGER NOT NULL
  ,FOREIGN KEY(id_dice) REFERENCES dice(id)
  ,FOREIGN KEY(id_side) REFERENCES dice_side(id)
);