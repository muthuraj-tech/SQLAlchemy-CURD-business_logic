from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


#initiate app
app = Flask(__name__)

app.config.from_pyfile('config.py')

#Init database
db = SQLAlchemy(app)
#Init marshmallow
ma = Marshmallow(app)

from views import *


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)