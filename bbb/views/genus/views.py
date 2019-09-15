from flask import render_template
from . import genus
from bbb.models.genus import Genus
from bbb import db

@genus.route('/genus')
def list_genus():
    all_genus = db.session.query(Genus).all()
    return render_template('genus/genus.html', items=all_genus)