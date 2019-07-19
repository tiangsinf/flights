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
    flight = int(request.form.get('flight'))
        
    # check if selected flight exist
    if Flight.query.filter(Flight.id == flight).first() is None:
        return flash('Invalid Flight ID')
    
    # add passenger to table
    add_passenger = Passenger(name = name, flight_id = flight)
    db.session.add(add_passenger)
    db.session.commit()

    return render_template('hello.html', name = name, flight = flight)

@main.route('/listing')
def flightList():
    flights = Flight.query.all()
    return render_template('flight_list.html', flights = flights)

@main.route('/flightDetails', methods=['POST'])
def flightDetails():
    flight_id = int(request.form.get('flight'))
    f = Flight.query.filter(Flight.id == flight_id).first()
    id = f.id
    origin = f.origin
    destination = f.destination
    duration = f.duration

    ps = Passenger.query.filter(Passenger.flight_id == flight_id).all()

    return render_template('flight_details.html', ps = ps, id = id, origin = origin, destination = destination, duration = duration)