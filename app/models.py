import os
from app import db

class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key = True)
    origin = db.Column(db.String(120), index = True, nullable = False)
    destination = db.Column(db.String(120), index = True, nullable = False)
    duration = db.Column(db.Integer, nullable = False)
    passenger = db.relationship('Passenger', backref = 'flights')

    def __repr__(self):
        return f'<Origin: {self.origin}, Destination: {self.destination}>'

class Passenger(db.Model):
    __tablename__ = 'passengers'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, nullable = False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'))

    def __repr__(self):
        return f'<Name: {self.name}>'

