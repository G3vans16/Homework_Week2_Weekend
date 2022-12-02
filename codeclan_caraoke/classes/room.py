class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guest_list = []
        self.song_playing = {}

    def check_in(self, guest):
        if guest.in_room == False and self.check_full_capacity() == False:
            self.guest_list.append(guest.name)
            guest.enter_room()

    def check_out(self, guest):
        if guest.name in self.guest_list:
            self.guest_list.remove(guest.name)
            guest.leave_room()

    def play_song(self, song):
        self.song_playing.clear()
        self.song_playing.update({song.title : song.artist})

    def check_full_capacity(self):
        if len(self.guest_list) >= self.capacity:
            return True
        else: return False
