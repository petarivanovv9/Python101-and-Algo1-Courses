from __future__ import print_function
from song import Song
from playlist import Playlist
import os
import glob
# import sys
# import re
# import mutagen
# from mutagen.id3 import ID3
from mutagen.mp3 import MP3
# rom mutagen.mp3 import MPEGInfo
# from mutagen.id3 import TPE1, TPE2


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        songs = []
        os.chdir(self.path)

        for item in glob.glob("*.mp3"):
            songs += [item]

        # mediafile = ID3(songs[3])
        # metadata = mediafile.pprint()
        new_playlist = Playlist("Peshko")

        for song in songs:
            audio = MP3(song)
            if 'TIT2' in audio.keys():
                current_title = audio['TIT2']
                # print (audio['TIT2'])  # name of the song - title
            else:
                current_title = ''
            if 'TPE1' in audio.keys():
                current_artist = audio['TPE1']
                # print (audio['TPE1'])  # name of the artist - artist
            else:
                current_artist = ''
            if 'TALB' in audio.keys():
                current_album = audio['TALB']
                # print (audio['TALB'])  # name of the album - album
            else:
                current_album = ''
            current_length = audio.info.length

            new_playlist.songs_list.append(
                Song(current_title, current_artist, current_album, current_length))

        # audio = MP3(songs[3])
        # # print (metadata)
        # print (10 * '-')
        # print (audio.info.length)

        # print (10 * '-')

        # print (songs[3])

        # print (10 * '-')

        # for song in new_playlist.songs_list:
        #     print (song)

        # new_playlist.pprint_playlist()

        return new_playlist



crawler = MusicCrawler("/home/petar-ivanov/Desktop/BAM/")


new_playlist = crawler.generate_playlist()

new_playlist.pprint_playlist()
