import unittest
import time
from song import Song
from playlist import Playlist


class TestSong(unittest .TestCase):

    def setUp(self):
        self.code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        self.song = Song(
            title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.code_songs.add_song(self.song)

    def test_create_new_playlist(self):
        self.assertEqual(self.code_songs.name, "Code")
        self.assertEqual(self.code_songs.repeat, True)
        self.assertEqual(self.code_songs.shuffle, True)

    def test_add_song(self):
        self.assertTrue(self.song in self.code_songs.songs_list)

    def test_remove_song(self):
        self.code_songs.remove_song(self.song)
        self.assertFalse(self.song in self.code_songs.songs_list)

    def test_add_songs(self):
        song1 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:44")
        song3 = Song(
            title="Odin3", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [song1, song2, song3]
        self.code_songs.add_songs(songs)
        self.assertTrue(song1 in self.code_songs.songs_list)
        self.assertTrue(song2 in self.code_songs.songs_list)
        self.assertTrue(song3 in self.code_songs.songs_list)

    def test_total_length(self):
        song1 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [song1, song2]
        self.code_songs.add_songs(songs)

        self.assertEqual(self.code_songs.total_length(), '11:12')

    def test_get_artists(self):
        song1 = Song(
            title="Odin", artist="Peshko", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin", artist="Peshko", album="The Sons of Odin", length="3:44")
        songs = [self.song, song1, song2]
        self.code_songs.add_songs(songs)

        counter_peshko = self.code_songs.get_artists()['Peshko']
        self.assertTrue(counter_peshko == 2)

    def test_next_song(self):
        song1 = Song(
            title="Bum", artist="Peshko", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Goooodsadas", artist="Peshko",
                     album="The Sons of Odin", length="3:44")
        songs = [self.song, song1, song2]
        self.code_songs.add_songs(songs)

        self.assertIsInstance(self.code_songs.next_song(), Song)

    # def test_load(self):
    #     p = Playlist.load("Manowar-songs.json")
    #     try:
    #         while True:
    #             song = p.next_song()
    #             print (str(song))
    #             time.sleep(1)
    #     except Exception as e:
    #         print (e)

    def test_save(self):
        s = Song(album="The Sons of Odin", title="Odin",
                 artist="Manowar", length="3:44")
        s1 = Song(album="The Sonds of Odin", title="Sons of Odin",
                  artist="Manowar", length="6:08")
        p = Playlist("Manowar songs", repeat="SONG")
        p.add_song(s)
        p.add_song(s1)
        p.add_song(Song(album="Fallen", title="Bring Me To Life (radio edit)",
                        artist="Evanesence", length="3:30"))

        p.pprint_playlist()

        p.save()

if __name__ == '__main__':
    unittest.main()
