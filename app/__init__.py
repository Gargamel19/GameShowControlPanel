from flask import Flask
import app.config as config

app = Flask(__name__)
app.config.from_object(config)

from app import routes