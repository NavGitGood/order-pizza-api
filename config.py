import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
app = connexion.App(__name__, specification_dir='./templates')

# Get the underlying Flask app instance
flask_app = app.app

# Configure the SqlAlchemy part of the app instance
flask_app.config["SQLALCHEMY_ECHO"] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///orders.db')
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
flask_app.config['JWT_SECRET_KEY'] = 'mdhs.me'

# JWT instance
jwt = JWTManager(flask_app)

# Create the SqlAlchemy db instance
db = SQLAlchemy(flask_app)

# Initialize Marshmallow
ma = Marshmallow(flask_app)
