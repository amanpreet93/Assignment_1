from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debug import Debug

app = Flask(__name__)
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"


app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)
#migrate = Migrate(app, db)

from app import  models
from app import views