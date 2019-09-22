from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from . import genus
from bbb.models import Genus
from bbb import db

@genus.route('/genus/')
def list_genus():
    all_genus = db.session.query(Genus).all()
    return render_template('genus/genus.html', items=all_genus)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    desc = TextAreaField('Description:')

@genus.route('/genus/new/', methods=['GET', 'POST'])
def new_genus():
    g = Genus()
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        g.name = request.form['name']
        g.desc = request.form['desc']

        if form.validate():
            flash ('Saving Genus ')
            s = db.session()
            s.add(g)
            s.commit()
        
        else:
            flash('Unable to save Genus')
    return render_template('common/form2.html', form=form, table="Genus")

@genus.route('/genus/<int:id>/edit/', methods=['GET', 'POST'])
def edit_genus(id):
    qry = db.session.query(Genus).filter(Genus.id==id)
    g = qry.first()
    form = ReusableForm(request.form, obj=g)
    if request.method == 'POST':
        g.name = request.form['name']
        g.desc = request.form['desc']

        if form.validate():
            flash ('Saving Genus ')
            s = db.session()
            s.add(g)
            s.commit()
        
        else:
            flash('Unable to save Genus')
    return render_template('common/form2.html', form=form, table='Genus')

@genus.route('/genus/<int:id>/')
def show_genus(id):
    print("ID: {}".format(id))
    qry = db.session.query(Genus).filter(Genus.id == id)
    item = qry.first()
    return render_template('genus/show.html', item=item, plants=item.plants, bugs=item.bugs)