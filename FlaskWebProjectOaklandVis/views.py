"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProjectOaklandVis import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/data')
def data():
    """Renders the home page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
    )

@app.route('/map')
def map():
    """Renders the home page."""
    return render_template(
        'map.html',
        title='Map',
        year=datetime.now().year,
    )

@app.route('/profile')
def profile():
    """Renders the profile page."""
    return render_template(
        'profile.html',
        title='Profile',
        year=datetime.now().year,
        message='Your profile page.'
    )

@app.route('/messages')
def messages():
    """Renders the messages page."""
    return render_template(
        'messages.html',
        title='Messages',
        year=datetime.now().year,
        message='Your messages page.'
    )
@app.route('/alert')
def alert():
    """Renders the profile page."""
    return render_template(
        'alert.html',
        title='Alert',
        year=datetime.now().year,
        message='Your alerts page.'
    )
@app.route('/signup')
def signup():
    """Renders the profile page."""
    return render_template(
        'signup.html',
        title='Signup',
        year=datetime.now().year,
        message='Your signup page.'
    )
