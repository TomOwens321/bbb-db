from flask import Blueprint

genus = Blueprint('genus', __name__)

from . import routes