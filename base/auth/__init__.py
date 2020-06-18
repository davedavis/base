# Blueprint that contains the user login and registration functionality forms and view logic.
from flask import Blueprint
auth = Blueprint('auth', __name__)

# Need to import this after the blueprint is initialized.
# Not importing the forms file as views already imports it.
from . import views

