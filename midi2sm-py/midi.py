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
    
    def getTime() -> int:
        return self.time
    
class Note(Event):
    def __init__(self):
        super(Event).__init__(self)
        self.pitch = 0
        self.velocity = 0
        self.channel = 0

# Event Types