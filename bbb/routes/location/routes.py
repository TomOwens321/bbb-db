from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, DecimalField
from . import location
from bbb.models import Location
from bbb import db

class ReusableForm(Form):
    name = StringField('Name: ', validators=[validators.DataRequired()])
    state = StringField('State: ')
    city = StringField('City: ')
    latitude = DecimalField('Latitude: ')
    longitude = DecimalField('Longitude: ')
    altitude = DecimalField('Altitude: ')
    desc = TextAreaField('Description: ')


@location.route('/location/')
def list_locations():
    all_locations = db.session.query(Location).all()
    return render_template('location/location.html', items=all_locations)