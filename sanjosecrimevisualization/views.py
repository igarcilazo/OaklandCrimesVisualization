"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from sanjosecrimevisualization import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Crimes',
        year=datetime.now().year,
    )

@app.route('/activities')
def activities():
    """Renders the home page."""
    return render_template(
        'activities.html',
        title='Activities',
        year=datetime.now().year,
    )

@app.route('/income')
def income():
    """Renders the home page."""
    return render_template(
        'income.html',
        title='Income',
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
@app.route('/covid')
def covid():
    """Renders the profile page."""
    return render_template(
        'covid.html',
        title='Covid',
        year=datetime.now().year,
        message='Your covid page.'
    )
