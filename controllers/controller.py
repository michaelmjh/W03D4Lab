from app import app
from flask import render_template, request
from models.events_list import events

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/events")
def show_events():
    return render_template('events_list.html', title='Events List', events=events)

@app.route("/add_event")
def add_event():
    return render_template("add_event.html", title="add event")
