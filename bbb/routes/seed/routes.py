from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from . import seed
from bbb.models import Seed
from bbb import db

@seed.route('/seed/')
def list_seeds():
    all_seeds = db.session.query(Seed).all()
    return render_template('seed/seed.html', items=all_seeds)