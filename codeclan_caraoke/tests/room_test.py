import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 3, 10.00)
        self.room2 = Room(2, 2, 10.00)
        self.guest = Guest("Gareth", 10.00)
        self.guest2 = Guest("Chris", 15.00)
        self.guest3 = Guest("Sam", 12.00)
        self.guest4 = Guest("Andrew", 0.00)
        self.song = Song("Sweet Caroline", "Neil Diamond")
        self.song2 = Song("Suspicious Minds", "Elvis Presley")

    def test_room_number(self):
        self.assertEqual(1, self.room.number)

    def test_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(["Gareth"], self.room.guest_list)

    def test_check_in_multiple_guests(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest2)
        self.assertEqual(["Gareth", "Chris"], self.room.guest_list)

    def test_check_in_already_in_room(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.assertEqual(["Gareth"], self.room.guest_list)

    def test_check_in_same_guest_multiple_rooms(self):
        self.room.check_in(self.guest)
        self.room2.check_in(self.guest)
        self.assertEqual(["Gareth"], self.room.guest_list)
        self.assertEqual([], self.room2.guest_list)

    def test_check_out(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual([], self.room.guest_list)

    def test_check_out_not_in_room(self):
        self.room.check_out(self.guest)
        self.assertEqual([], self.room.guest_list)

    def test_play_song(self):
        self.room.play_song(self.song)
        self.assertEqual({"Sweet Caroline" : "Neil Diamond"}, self.room.song_playing)

    def test_play_song_already_playing(self):
        self.room.play_song(self.song)
        self.room.play_song(self.song2)
        self.assertEqual({"Suspicious Minds" : "Elvis Presley"}, self.room.song_playing)

    def test_room_capacity(self):
        self.assertEqual(3, self.room.capacity)

    def test_room_capacity_full(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest2)
        self.room.check_in(self.guest3)
        result = self.room.check_full_capacity()
        self.assertEqual(True, result)

    def test_room_capacity_not_full(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest2)
        result = self.room.check_full_capacity()
        self.assertEqual(False, result)

    def test_check_in_if_room_is_full(self):
        self.room2.check_in(self.guest)
        self.room2.check_in(self.guest2)
        self.room2.check_in(self.guest3)
        self.assertEqual(["Gareth", "Chris"], self.room2.guest_list)

    def test_check_in_if_room_has_space(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest2)
        self.room.check_in(self.guest3)
        self.assertEqual(["Gareth", "Chris", "Sam"], self.room.guest_list)

    def test_room_price(self):
        self.assertEqual(10, self.room.price)

    def test_charge_guest(self):
        self.room.charge_guest(self.guest)
        self.assertEqual(10, self.room.till)
        self.assertEqual(0, self.guest.wallet)

    def test_charge_guest_cant_afford_room(self):
        self.room.charge_guest(self.guest4)
        self.assertEqual(0, self.room.till)
        self.assertEqual(0, self.guest4.wallet)

    def test_check_in_and_charge_guest(self):
        self.room.check_in_and_charge_guest(self.guest)
        self.assertEqual(["Gareth"], self.room.guest_list)
        self.assertEqual(10, self.room.till)
        self.assertEqual(0, self.guest.wallet)

    def test_check_in_and_charge_guest_cant_afford(self):
        self.room.check_in_and_charge_guest(self.guest4)
        self.assertEqual([], self.room.guest_list)
        self.assertEqual(0, self.room.till)
        self.assertEqual(0, self.guest4.wallet)