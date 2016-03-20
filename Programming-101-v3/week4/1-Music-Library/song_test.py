from song import Song
import unittest


class TestSong(unittest .TestCase):

    def setUp(self):
        self.song = Song(
            title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

    def test_create_new_song(self):
        self.assertTrue(isinstance(self.song, Song))
        self.assertEqual(self.song.title, 'Odin')
        self.assertEqual(self.song.artist, 'Manowar')
        self.assertEqual(self.song.album, "The Sons of Odin")
        self.assertEqual(self.song.length, "3:44")

    def test_str(self):
        message = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(str(self.song), message)

    def test_hash(self):
        self.assertTrue(isinstance(hash(self.song), int))

    def test_eq(self):
        song2 = Song(
            title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        song3 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertTrue(song2 == self.song)
        self.assertFalse(song3 == self.song)

    def test_length(self):
        self.assertEqual(self.song.get_length('seconds'), 224)
        self.assertEqual(self.song.get_length('minutes'), 3)
        self.assertEqual(self.song.get_length('hours'), 0)


if __name__ == '__main__':
    unittest.main()
