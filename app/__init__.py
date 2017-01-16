from flask import Flask
from .book import book

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.release')
app.config.from_pyfile('config.py')

app.register_blueprint(book)