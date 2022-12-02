import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1)
        self.room2 = Room(2)
        self.guest = Guest("Gareth")
        self.song = Song("Sweet Caroline", "Neil Diamond")

    def test_room_number(self):
        self.assertEqual(1, self.room.number)

    def test_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(["Gareth"], self.room.guest_list)

    # def test_check_in_already_in

    def test_check_out(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual([], self.room.guest_list)

    def test_play_song(self):
        self.room.play_song(self.song)
        self.assertEqual({"Sweet Caroline" : "Neil Diamond"}, self.room.song_playing)
    
    # def test_check_in(self):
    #     self.room.check_in(self.guest, self.room.number)
    #     self.assertEqual({1 : "Gareth"}, self.room.guest_list)

    # def test_check_out(self):
    #     self.room.check_out(self.guest, self.room.number)
    #     self.assertEqual({1 : "Gareth"}, self.room.guest_list)