from flask import render_template, flash, request
from wtforms import Form, DateField, IntegerField, validators, StringField, SubmitField
from . import seed
from bbb.models import Seed, Flora, Location
from bbb import db
from dateutil import parser

class ReusableForm(Form):
    flora_name = StringField('Plant: ')
    location_name = StringField('Location: ')
    quantity = IntegerField('Quantity: ')
    uom = StringField('Unit of Measure: ')
    collection_date = DateField('Collection Date: ')
    collection_lot  = StringField('Collection Lot: ')
    analysis_lot    = StringField('Analysis Lot: ')
    analysis_date   = DateField('Analysis Date: ')

def flat_list(l):
    return ["%s" % v for v in l]

def _exists(table, value):
    s = db.session()
    r = s.query(table).filter(table.name==value).first()
    if not r:
        print("New record!")
        r = table(name=value)
        s.add(r)
        s.commit()
    return r

@seed.route('/seed/')
def list_seeds():
    all_seeds = db.session.query(Seed).all()
    return render_template('seed/seed.html', items=all_seeds)

@seed.route('/seed/new/', methods=['GET', 'POST'])
@seed.route('/seed/<int:id>/edit/', methods=['GET', 'POST'])
def new_seed(id=None):
    if id:
        seed = db.session.query(Seed).filter(Seed.id==id).first()
        form = ReusableForm(request.form, obj=seed)
    else:
        seed = Seed()
        form = ReusableForm(request.form)
    plant_list = flat_list(db.session.query(Flora.name).all())
    location_list = flat_list(db.session.query(Location.name).all())
    if request.method == 'POST':
        seed.flora = _exists(Flora, request.form['flora_name'])
        seed.location = _exists(Location, request.form['location_name'])
        seed.quantity = request.form['quantity']
        seed.uom      = request.form['uom']
        if request.form['collection_date']:
            seed.collection_date = parser.parse(request.form['collection_date'])
        seed.collection_lot  = request.form['collection_lot']
        if request.form['analysis_date']:
            seed.analysis_date   = parser.parse(request.form['analysis_date'])
        seed.analysis_lot    = request.form['analysis_lot']
        session = db.session()
        session.add(seed)
        session.commit()
        session.close()
        flash("Saving Seed")

    return render_template('seed/form.html', form=form, fl=plant_list, ll=location_list)

@seed.route('/seed/<int:id>/')
def show_seed(id):
    seed = db.session.query(Seed).filter(Seed.id==id).first()
    return render_template('seed/show.html', seed=seed)