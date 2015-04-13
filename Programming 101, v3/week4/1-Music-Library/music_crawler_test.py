import unittest
from music_crawler import MusicCrawler


class Test_MusicCrawler(unittest.TestCase):

    def setUp(self):
        path = '/home/petar-ivanov/Desktop/Music/'
        self.crawler = MusicCrawler(path)

    def test_generate_playlist(self):
        playlist = self.crawler.generate_playlist()

        self.assertEqual(str(playlist.songs_list[0]), 'Alex P. - Belucci (mp3zoneBG.net) from [mp3zoneBG.net] - 0:02:42')


if __name__ == '__main__':
    unittest.main()
