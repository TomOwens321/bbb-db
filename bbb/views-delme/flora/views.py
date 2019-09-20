from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from bbb.models import Flora, Genus, Species
from bbb import db
from . import flora

class ReusableForm(Form):
    genus = StringField('Genus: ', validators=[validators.required()])
    species = StringField('Species: ', validators=[validators.required()])
    common_name = StringField('Common Name: ')
    desc = TextAreaField('Description: ')
    sub_species = StringField('Sub Species: ')
    variety = StringField('Variety: ')
    germination_code = StringField('Germination Code: ')

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
    #s.close()
    # print(r)
    return r

@flora.route('/flora')
def list_flora():
    all_flora = db.session.query(Flora).all()
    return render_template("flora/flora.html", items=all_flora)

@flora.route('/flora/new', methods=['GET', 'POST'])
def new_flora():
    plant = Flora()
    genus_list = flat_list(db.session.query(Genus.name).all())
    species_list = flat_list(db.session.query(Species.name).all())
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        plant.genus = request.form['genus']
        plant.species = request.form['species']
        plant.common_name = request.form['common_name']
        plant.desc = request.form['desc']
        plant.germination_code = request.form['germination_code']
        plant.sub_species = request.form['sub_species']
        plant.variety = request.form['variety']

        if form.validate():
            session = db.session()
            g = _exists(Genus,plant.genus)
            s = _exists(Species,plant.species)
            plant.genus = g
            plant.species = s
            session.add(plant)
            session.commit()
            session.close()

        else:
            flash('Unable to save Flora')
    return render_template('flora/form.html', form=form, gl=genus_list, sl=species_list)
