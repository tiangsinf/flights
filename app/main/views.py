# import all modules from plugins
from flask import render_template, request, session, redirect, url_for, flash
from . import main
from .. import db
from app.models import *

@main.route('/')
@main.route('/booking' methods=['GET', 'POST'])
def index():
    flights = Flight.query.all()
    if request.method == 'POST':
        flight = request.form['flights'].id
    else:
        flash('Invalid Request Method. Please use form.')
    return render_template('index.html', flights = flights)