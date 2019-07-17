import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

def main():
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Flight=Flight, Passenger=Passenger)

if __name__ == "__main__":
    with app.app_context():
        main()