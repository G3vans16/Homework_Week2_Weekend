import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Sweet Caroline", "Neil Diamond")
        self.song2 = Song("Suspicious Minds", "Elvis Presley")
        self.song3 = Song("Rolling in the Deep", "Adele")

    def test_song_title(self):
        self.assertEqual("Sweet Caroline", self.song.title)

    def test_song_artist(self):
        self.assertEqual("Neil Diamond", self.song.artist)