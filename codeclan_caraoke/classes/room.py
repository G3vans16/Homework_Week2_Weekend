class Room:
    def __init__(self, number):
        self.number = number
        self.guest_list = []
        self.song_playing = {}

    def check_in(self, guest):
        self.guest_list.append(guest.name)
        # self.guest_list.update({room_number : guest.name})

    def check_out(self, guest):
        self.guest_list.remove(guest.name)

    def play_song(self, song):
        self.song_playing.update({song.title : song.artist})
