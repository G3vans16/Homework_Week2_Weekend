class Room:
    def __init__(self, number):
        self.number = number
        self.guest_list = []

    def check_in(self, guest, room_number):
        