# import all modules from plugins
from flask import render_template, request, session, redirect, url_for, flash
from . import main
from .. import db
from app.models import *

@main.route('/')
@main.route('/home')
def index():
    flights = Flight.query.all()
    return render_template('index.html', flights = flights)

@main.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    flight = request.form.get('flight')
    return render_template('hello.html', name=name, flight=flight)