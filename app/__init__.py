from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.release')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from .book import models, book

app.register_blueprint(book)
