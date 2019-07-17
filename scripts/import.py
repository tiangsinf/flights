import os
import csv
from app import create_app, db
from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

def main():
    f = open('import.csv')
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()