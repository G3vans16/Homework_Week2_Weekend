import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Gareth", 10.00)
        self.guest2 = Guest("Chris", 15.00)
        self.guest3 = Guest("Sam", 12.00)
        self.room = Room(1, 3, 10.00)

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

    def test_pay_money(self):
        self.guest.pay_money(self.room)
        self.assertEqual(0, self.guest.wallet)