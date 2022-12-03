class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.in_room = False
        self.wallet = wallet

    def enter_room(self):
        self.in_room = True

    def leave_room(self):
        self.in_room = False

    def pay_money(self, room):
        self.wallet -= room.price