import os

from project_webber.app import app

def main():
  os.environ["FLASK_ENV"] = "development"
  app.run("0.0.0.0", debug=True)
