from flask import render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from bbb.models import Fauna, Genus, Species, Flora
from bbb import db
from . import fauna

class ReusableForm(Form):
    genus_name = StringField('Genus: ', validators=[validators.required()])
    species_name = StringField('Species: ', validators=[validators.required()])
    common_name = StringField('Common Name: ')
    desc = TextAreaField('Description: ')
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
    return r

@fauna.route('/fauna/')
def list_fauna():
    all_fauna = db.session.query(Fauna).all()
    return render_template("fauna/fauna.html", items=all_fauna)

@fauna.route('/fauna/new/', methods=['GET', 'POST'])
@fauna.route('/fauna/<int:id>/edit/', methods=['GET', 'POST'])
def new_fauna(id=None):
    if id:
        bug = db.session.query(Fauna).filter(Fauna.id == id).first()
        form = ReusableForm(request.form, obj=bug)
    else:
        bug = Fauna()
        form = ReusableForm(request.form)
    genus_list = flat_list(db.session.query(Genus.name).all())
    species_list = flat_list(db.session.query(Species.name).all())
    print(form.errors)
    if request.method == 'POST':
        bug.genus = _exists(Genus, request.form['genus_name'])
        bug.species = _exists(Species, request.form['species_name'])
        bug.common_name = request.form['common_name']
        bug.desc = request.form['desc']

        if form.validate():
            session = db.session()
            g = _exists(Genus,bug.genus)
            s = _exists(Species,bug.species)
            bug.genus = g
            bug.species = s
            session.add(bug)
            session.commit()
            session.close()

        else:
            flash('Unable to save Fauna')
    return render_template('fauna/form.html', form=form, gl=genus_list, sl=species_list)

@fauna.route('/fauna/<int:id>/')
def show_fauna(id=None):
    fauna = db.session.query(Fauna).filter(Fauna.id == id).first()
    return render_template('fauna/show.html', fauna=fauna)

@fauna.route('/fauna/<int:id>/association/', methods=['GET', 'POST'])
def associate_fauna(id=None):
    a_plants = []
    n_plants = []
    bug = db.session.query(Fauna).filter(Fauna.id == id).first()
    plant_list = db.session.query(Flora).all()
    for p in plant_list:
        if p in bug.plants:
            a_plants.append(p)
        else:
            n_plants.append(p)
    if request.method == 'POST':
        print("Requested {}".format(request.form['plant']))
        plant = db.session.query(Flora).filter(Flora.id == request.form['plant']).first()
        if request.form['assoc'] == 'associate':
            print("Associating {}".format(plant.id))
            bug.plants.append(plant)
        if request.form['assoc'] == 'dissociate':
            bug.plants.remove(plant)
        s = db.session()
        s.add(bug)
        s.commit()
        return redirect("/fauna/{}/association/".format(bug.id))
    return render_template('/fauna/assoc.html', bug=bug, a_plants=a_plants, n_plants=n_plants)