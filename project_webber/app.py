from flask import Flask, render_template

from project_webber.utils.db import db_query, db_commit, db_execute
from project_webber.utils.dice import dice_create, dice_all


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', dice=dice_all())
