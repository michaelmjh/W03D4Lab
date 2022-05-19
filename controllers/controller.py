from crypt import methods
from app import app
from flask import render_template, request
from models.events_list import *

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/events")
def show_events():
    return render_template('events_list.html', title='Events List', events=events)

@app.route("/add_event")
def show_add_event():
    return render_template("add_event.html", title="add event")

@app.route("/add_event", methods=['POST'])
def add_event():
   
    e_date = request.form['date']
    e_name = request.form['name']
    e_number_of_guests = request.form['number_of_guests']
    e_room_location = request.form['room_location']
    e_description = request.form['description']

    new_event = Event(e_date, e_name, e_number_of_guests, e_room_location, e_description)
    add_new_event(new_event)
    return render_template('events_list.html', title='Events List', events=events)

