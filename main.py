class MidiLexer:
    def __init__(self):
        self.events = []
        self.notes = []
        self.text_events = []
        self.tempo_changes = []