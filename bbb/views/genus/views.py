from flask import render_template
from . import genus
from bbb.models.genus import Genus
from ... import db

@genus.route('/genus')
def list_genus():
    list = Genus.query.all()
    return render_template('genus/genus.html', genus=list)