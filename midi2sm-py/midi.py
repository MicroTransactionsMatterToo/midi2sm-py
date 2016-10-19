class MIDIFileParser:
    def __init__(self):
        self.events = []
        self.notes = []
        self.text_events = []
        self.tempo_changes = []
        self.system_events = []
    

# Base Classes

class Event:
    def __init__(self):
        # All MIDI Events have a timestamp
        self.time = 0

# Event Types