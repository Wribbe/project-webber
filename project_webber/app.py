from flask import Flask, render_template

from project_webber.utils import db_query, db_commit, db_execute
from project_webber.utils import dice_create

app = Flask(__name__)

@app.route('/')
def index():
  add_stuff()
  return render_template('index.html')

def add_stuff():
  dice1 = dice_create(range(1,7))
  dice2 = dice_create(["A","B","C"])
