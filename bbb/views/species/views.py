from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from . import species
from bbb.models.species import Species
from bbb import db

@species.route('/species')
def list_species():
    all_species = db.session.query(Species).all()
    return render_template('species/species.html', items=all_species)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    desc = TextAreaField('Description:')

@species.route('/species/new', methods=['GET', 'POST'])
def new_species():
    g = Species()
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        g.name = request.form['name']
        g.desc = request.form['desc']

        if form.validate():
            flash ('Saving Species ')
            s = db.session()
            s.add(g)
            s.commit()
        
        else:
            flash('Unable to save Species')
    return render_template('species/form.html', form=form)

@species.route('/species/edit/<int:id>', methods=['GET', 'POST'])
def edit_species(id):
    qry = db.session.query(Species).filter(Species.id==id)
    g = qry.first()
    form = ReusableForm(request.form, obj=g)
    if request.method == 'POST':
        g.name = request.form['name']
        g.desc = request.form['desc']

        if form.validate():
            flash ('Saving Species ')
            s = db.session()
            s.add(g)
            s.commit()
        
        else:
            flash('Unable to save Species')
    return render_template('species/form.html', form=form)

@species.route('/species/show/<int:id>')
def show_species(id):
    print("ID: {}".format(id))
    qry = db.session.query(Species).filter(Species.id == id)
    item = qry.first()
    return render_template('species/show.html', item=item)