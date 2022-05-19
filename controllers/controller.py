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
    e_recurring = request.form['recurring']
    if e_recurring == 1:
        e_recurring = True
    else:
        e_recurring = False
    e_description = request.form['description']

    new_event = Event(e_date, e_name, e_number_of_guests, e_room_location, e_description, e_recurring)
    add_new_event(new_event)
    return render_template('events_list.html', title='Events List', events=events)

@app.route("/remove_event")
def show_remove_event():
    return render_template("remove_event.html", title="remove event", events=events)

@app.route("/remove_event", methods=['POST'])
def remove_event():
    event = request.form
    print(event["events"])
    remove_event_func(event)
    return render_template('events_list.html', title='Events List', events=events)

