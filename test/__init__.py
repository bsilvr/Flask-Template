import sys,os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

sys.path.insert(1, os.path.join(sys.path[0], '..'))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://es:es-test@localhost:5432/usermanagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())

import test.models
import test.views

import test2.models
import test2.views
