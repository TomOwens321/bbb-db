from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from . import family
from bbb.models import Family
from bbb import db

@family.route('/family/')
def list_family():
    all_family = db.session.query(Family).all()
    return render_template('family/family.html', items=all_family)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    desc = TextAreaField('Description:')

@family.route('/family/new/', methods=['GET', 'POST'])
def new_family():
    g = Family()
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        g.name = request.form['name']
        g.desc = request.form['desc']

        if form.validate():
            flash ('Saving Family ')
            s = db.session()
            s.add(g)
            s.commit()
        
        else:
            flash('Unable to save Family')
    return render_template('common/form2.html', form=form, table='Family')

@family.route('/family/<int:id>/edit/', methods=['GET', 'POST'])
def edit_family(id):
    qry = db.session.query(Family).filter(Family.id==id)
    g = qry.first()
    form = ReusableForm(request.form, obj=g)
    if request.method == 'POST':
        g.name = request.form['name']
        g.desc = request.form['desc']

        if form.validate():
            flash ('Saving Family ')
            s = db.session()
            s.add(g)
            s.commit()
        
        else:
            flash('Unable to save Family')
    return render_template('common/form2.html', form=form, table='Family')

@family.route('/family/<int:id>/')
def show_family(id):
    print("ID: {}".format(id))
    qry = db.session.query(Family).filter(Family.id == id)
    item = qry.first()
    return render_template('family/show.html', item=item, plants=item.plants, bugs=item.bugs)