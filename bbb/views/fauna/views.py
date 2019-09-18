from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from bbb.models import Fauna, Genus, Species
from bbb import db
from . import fauna

class ReusableForm(Form):
    genus = StringField('Genus: ', validators=[validators.required()])
    species = StringField('Species: ', validators=[validators.required()])
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
    #s.close()
    print(r)
    return r

@fauna.route('/fauna')
def list_fauna():
    all_fauna = db.session.query(Fauna).all()
    return render_template("fauna/fauna.html", items=all_fauna)

@fauna.route('/fauna/new', methods=['GET', 'POST'])
def new_fauna():
    bug = Fauna()
    genus_list = flat_list(db.session.query(Genus.name).all())
    species_list = flat_list(db.session.query(Species.name).all())
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        bug.genus = request.form['genus']
        bug.species = request.form['species']
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
