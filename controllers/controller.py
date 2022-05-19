from app import app
from flask import render_template
from models.events_list import events

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def show_events():
    return render_template('index.html', title='Events List', events=events)