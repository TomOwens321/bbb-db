from flask import Blueprint

flora = Blueprint('flora', __name__)

from . import views