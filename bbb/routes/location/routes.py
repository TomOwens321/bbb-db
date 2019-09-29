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

@location.route('/location/new/', methods=['GET', 'POST'])
@location.route('/location/<int:id>/edit/', methods=['GET', 'POST'])
def new_location(id=None):
    if id:
        location = db.session.query(Location).filter(Location.id == id).first()
        form = ReusableForm(request.form, obj=location)
    else:
        location = Location()
        form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        location.name = request.form['name']
        location.state = request.form['state']
        location.city = request.form['city']
        location.latitude = request.form['latitude']
        location.longitude = request.form['longitude']
        location.altitude = request.form['altitude']
        location.desc = request.form['desc']

        if form.validate():
            session = db.session()
            session.add(location)
            session.commit()
            session.close()
            flash('Saving Location')

        else:
            flash('Unable to save Location')
    return render_template('location/form.html', form=form)