class Guest:
    def __init__(self, name):
        self.name = name
        self.in_room = False

    def enter_room(self):
        self.in_room = True

    def leave_room(self):
        self.in_room = False