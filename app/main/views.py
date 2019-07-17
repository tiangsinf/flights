# import all modules from plugins
from flask import render_template, session, redirect, url_for
from . import main
from .. import db

@main.route('/')
def index():
    return 'hello world'