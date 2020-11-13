from flask import Flask, render_template

from project_webber.utils import db_execute, db_commit

app = Flask(__name__)

@app.route('/')
def index():
  db_commit()
  return render_template('index.html')
