from flask import Blueprint

main = Blueprint('main', __name__)

# Import from all view files
from . import views, errors