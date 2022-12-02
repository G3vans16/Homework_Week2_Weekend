import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Gareth", 10)
        self.guest2 = Guest("Chris", 15)
        self.guest3 = Guest("Sam", 0)

    def test_guest_name(self):
        self.assertEqual("Gareth", self.guest.name)

    def test_guest_in_room(self):
        self.assertEqual(False, self.guest.in_room)

    def test_guest_enter_room(self):
        self.guest.enter_room()
        self.assertEqual(True, self.guest.in_room)

    def test_guest_leave_room(self):
        self.guest.leave_room()
        self.assertEqual(False, self.guest.in_room)

    def test_guest_wallet(self):
        self.assertEqual(10, self.guest.wallet)