# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField, HiddenField, RadioField, SelectField
from wtforms import validators

from babel import *

class GisForm(FlaskForm):
    latitude = StringField('Latitud')
    longitude = StringField('Longitud')
    radio = StringField('Radio (en Km.)')

class SearchForm(FlaskForm):
    text = TextField('Buscar')
