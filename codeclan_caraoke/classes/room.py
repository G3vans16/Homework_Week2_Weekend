class Room:
    def __init__(self, number):
        self.number = number
        self.guest_list = []
        self.song_playing = {}

    def check_in(self, guest):
        if guest.in_room == False:
            self.guest_list.append(guest.name)
            guest.enter_room()

    def check_out(self, guest):
        if guest.name in self.guest_list:
            self.guest_list.remove(guest.name)
            guest.leave_room()

    def play_song(self, song):
        self.song_playing.clear()
        self.song_playing.update({song.title : song.artist})
