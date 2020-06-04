from flask import Flask
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

from views import *

app.app_context().push()

if __name__ == '__main__':
    app.run()
