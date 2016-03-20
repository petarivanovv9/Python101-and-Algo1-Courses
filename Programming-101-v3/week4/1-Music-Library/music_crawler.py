from __future__ import print_function
from song import Song
from playlist import Playlist
import os
import glob
from mutagen.mp3 import MP3
import datetime


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        files_in_dir = [x for x in os.listdir(self.path) if x.endswith('.mp3')]
        songs = []
        os.chdir(self.path)

        for item in glob.glob("*.mp3"):
            songs += [item]

        new_playlist = Playlist("Peshko", True, True)

        for song in songs:
            audio = MP3(song)
            if 'TIT2' in audio.keys():
                current_title = str(audio['TIT2'])
            else:
                current_title = ''
            if 'TPE1' in audio.keys():
                current_artist = str(audio['TPE1'])
            else:
                current_artist = ''
            if 'TALB' in audio.keys():
                current_album = audio['TALB']
            else:
                current_album = ''
            current_length = str(
                datetime.timedelta(seconds=int(audio.info.length)))

            new_playlist.songs_list.append(
                Song(current_title, current_artist, current_album, current_length))

        return new_playlist
