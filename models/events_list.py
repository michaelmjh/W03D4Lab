from models.events import Event
from datetime import datetime

event_1 = Event(datetime(2022, 5, 19), "Drinks after Lab", 20, "Pig and Butterfly", "Stress relief")
event_2 = Event(datetime(2022, 5, 16), "Graduation", 30, "Pig and Butterfly", "Party time!")

events = [event_1, event_2]