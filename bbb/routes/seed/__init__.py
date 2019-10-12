from flask import Blueprint

seed = Blueprint('seed', __name__)

from . import routes