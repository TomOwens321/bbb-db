from flask import render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, DecimalField
from . import location
from bbb.models import Location, Flora
from bbb import db
from bbb.routes.helpers import smart_delete

class ReusableForm(Form):
    name = StringField('Name: ', validators=[validators.DataRequired()])
    state = StringField('State: ')
    city = StringField('City: ')
    latitude = StringField('Latitude: ')
    longitude = StringField('Longitude: ')
    altitude = StringField('Altitude: ')
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
        if request.form['latitude']:
            location.latitude = request.form['latitude']
        if request.form['longitude']:
            location.longitude = request.form['longitude']
        if request.form['altitude']:
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

@location.route('/location/<int:id>/')
def show_location(id=None):
    location = db.session.query(Location).filter(Location.id == id).first()
    return render_template('location/show.html', location=location)

@location.route('/location/<int:id>/association/', methods=['GET', 'POST'])
def associate_location(id=None):
    a_plants = []
    n_plants = []
    loc = db.session.query(Location).filter(Location.id == id).first()
    plant_list = db.session.query(Flora).all()
    for p in plant_list:
        if p in loc.plants:
            a_plants.append(p)
        else:
            n_plants.append(p)
    if request.method == 'POST':
        plant = db.session.query(Flora).filter(Flora.id == request.form['plant']).first()
        if request.form['assoc'] == 'associate':
            loc.plants.append(plant)
        if request.form['assoc'] == 'dissociate':
            loc.plants.remove(plant)
        s = db.session()
        s.add(loc)
        s.commit()
        return redirect("/location/{}/association/".format(loc.id))
    return render_template('/location/assoc.html', location=loc, a_plants=a_plants, n_plants=n_plants)

@location.route('/location/<int:id>/delete/')
def delete_location(id):
    location = db.session.query(Location).filter(Location.id==id).first()
    smart_delete(location)
    return redirect('/location/')