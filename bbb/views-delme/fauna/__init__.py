from flask import Blueprint

fauna = Blueprint('fauna', __name__)

from . import views