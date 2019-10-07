from flask import render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from bbb.models import Fauna, Genus, Species, Flora, Family
from bbb import db
from . import fauna

class ReusableForm(Form):
    family_name  = StringField('Family: ')
    genus_name   = StringField('Genus: ', validators=[validators.required()])
    species_name = StringField('Species: ', validators=[validators.required()])
    sub_species  = StringField('Sub Species: ')
    variety      = StringField('Variety: ')
    common_name  = StringField('Common Name: ')
    desc         = TextAreaField('Description: ')
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
    family_list  = flat_list(db.session.query(Family.name).all())
    genus_list   = flat_list(db.session.query(Genus.name).all())
    species_list = flat_list(db.session.query(Species.name).all())
    print(form.errors)
    if request.method == 'POST':
        bug.family = _exists(Family, request.form['family_name'])
        bug.genus = _exists(Genus, request.form['genus_name'])
        bug.species = _exists(Species, request.form['species_name'])
        bug.sub_species = request.form['sub_species']
        bug.variety = request.form['variety']
        bug.common_name = request.form['common_name']
        bug.desc = request.form['desc']
        bug.name = '{} {}'.format(bug.genus_name, bug.species_name)
        if bug.sub_species:
            bug.name += ' ssp:{}'.format(bug.sub_species)
        if bug.variety:
            bug.name += ' var:{}'.format(bug.variety)

        if form.validate():
            session = db.session()
            session.add(bug)
            session.commit()
            session.close()

        else:
            flash('Unable to save Fauna')
    return render_template('fauna/form.html', form=form, fl=family_list, gl=genus_list, sl=species_list)

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
        plant = db.session.query(Flora).filter(Flora.id == request.form['plant']).first()
        if request.form['assoc'] == 'associate':
            bug.plants.append(plant)
        if request.form['assoc'] == 'dissociate':
            bug.plants.remove(plant)
        s = db.session()
        s.add(bug)
        s.commit()
        return redirect("/fauna/{}/association/".format(bug.id))
    return render_template('/fauna/assoc.html', bug=bug, a_plants=a_plants, n_plants=n_plants)