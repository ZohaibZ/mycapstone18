from flask_wtf import FlaskForm
from application.models import *
from wtforms import TextField, validators, SelectField, SubmitField, SelectMultipleField, fields
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

# class scanning(Flaskform):
#     id =
