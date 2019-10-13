from flask import render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from bbb.models import Flora, Genus, Species, Family
from bbb import db
from . import flora
from bbb.routes.helpers import _exists, flat_list, smart_delete

class ReusableForm(Form):
    genus_name = StringField('Genus: ', validators=[validators.required()])
    species_name = StringField('Species: ', validators=[validators.required()])
    family_name = StringField('Family: ')
    common_name = StringField('Common Name: ')
    desc = TextAreaField('Description: ')
    sub_species = StringField('Sub Species: ')
    variety = StringField('Variety: ')
    germination_code = StringField('Germination Code: ')

@flora.route('/flora/')
def list_flora():
    all_flora = db.session.query(Flora).all()
    return render_template("flora/flora.html", items=all_flora)

@flora.route('/flora/new/', methods=['GET', 'POST'])
@flora.route('/flora/<int:id>/edit/', methods=['GET', 'POST'])
def new_flora(id=None):
    if id:
        plant = db.session.query(Flora).filter(Flora.id==id).first()
        form = ReusableForm(request.form, obj=plant)
    else:
        plant = Flora()
        form = ReusableForm(request.form)
    genus_list = flat_list(db.session.query(Genus.name).all())
    species_list = flat_list(db.session.query(Species.name).all())
    family_list = flat_list(db.session.query(Family.name).all())
    print(form.errors)
    if request.method == 'POST':
        plant.genus = _exists(Genus, request.form['genus_name'])
        plant.species = _exists(Species, request.form['species_name'])
        if request.form['family_name']:
            plant.family = _exists(Family, request.form['family_name'])
        plant.common_name = request.form['common_name']
        plant.desc = request.form['desc']
        plant.germination_code = request.form['germination_code']
        plant.sub_species = request.form['sub_species']
        plant.variety = request.form['variety']
        plant.name = '{} {}'.format(plant.genus_name,plant.species_name)
        if plant.sub_species:
            plant.name += ' ssp:{}'.format(plant.sub_species)
        if plant.variety:
            plant.name += ' var:{}'.format(plant.variety)
        if form.validate():
            session = db.session()
            session.add(plant)
            session.commit()
            flash('Saving Flora')
            return redirect('/flora/{}/'.format(plant.id))

        else:
            flash('Unable to save Flora')
    return render_template('flora/form.html', form=form, gl=genus_list, sl=species_list, fl=family_list, name=plant.name)

@flora.route('/flora/<int:id>/')
def show_flora(id):
    plant = db.session.query(Flora).filter(Flora.id == id).first()
    return render_template('flora/show.html', plant=plant)

@flora.route('/flora/<int:id>/delete/')
def delete_flora(id):
    plant = db.session.query(Flora).filter(Flora.id==id).first()
    smart_delete(Flora, plant)
    return redirect('/flora/')