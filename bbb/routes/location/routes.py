from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from . import location
from bbb.models import Location
from bbb import db

@seed.route('/location/')
def list_locations():
    all_locations = db.session.query(Location).all()
    return render_template('location/location.html', items=all_locations)