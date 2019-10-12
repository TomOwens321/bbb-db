from flask import Blueprint

species = Blueprint('species', __name__)

from . import views