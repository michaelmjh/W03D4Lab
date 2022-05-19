from models.events import Event
from datetime import datetime

event_1 = Event(datetime(2022, 5, 19), "Drinks after Lab", 20, "Pig and Butterfly", "Stress relief", False)
event_2 = Event(datetime(2022, 5, 16), "Graduation", 30, "Pig and Butterfly", "Party time!", False)

events = [event_1, event_2]

def add_new_event(event):
    events.append(event)

def remove_event(event):
    events.remove(event)