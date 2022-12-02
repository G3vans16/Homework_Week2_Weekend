import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Gareth")
        self.guest2 = Guest("Chris")
        self.guest3 = Guest("Gareth")

    def test_guest_name(self):
        self.assertEqual("Gareth", self.guest.name)