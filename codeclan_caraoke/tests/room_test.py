import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1)
        self.room2 = Room(2)
        self.room3 = Room(3)

    def test_room_number(self):
        self.assertEqual(1, self.room.number)

    def test_check_in(self, guest, room_number):
        
        self.assertEqual(["Gareth"], self.room.guest_list)