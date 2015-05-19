from song import Song
from random import randint
from tabulate import tabulate
import json


class Playlist:

    def __init__(self, name='Unknown', repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs_list = []
        self.copy_songs_list = []

    def add_song(self, song):
        self.songs_list.append(song)

    def remove_song(self, song):
        self.songs_list.remove(song)

    def add_songs(self, songs):
        self.songs_list += [song for song in songs]

    def total_length(self):

        sum_total_length = 0
        for song in self.songs_list:
            sum_total_length += song.get_length('seconds')

        hours = sum_total_length // 3600
        minutes = (sum_total_length - hours * 3600) // 60
        seconds = sum_total_length - hours * 3600 - minutes * 60

        if hours == 0:
            return '{}:{}'.format(minutes, seconds)
        else:
            return '{}:{}:{}'.format(hours, minutes, seconds)

    def get_artists(self):
        artists_histogram = {}
        artists = [x.artist for x in self.songs_list]

        for artist in artists:
            if artist in artists_histogram:
                artists_histogram[artist] += 1
            else:
                artists_histogram[artist] = 1

        return artists_histogram

    def next_song(self):
        if self.repeat is True:
            if self.shuffle is True:
                if len(self.songs_list) == 0:
                    self.songs_list = self.copy_songs_list[:]
                    self.copy_songs_list = []
                    size = len(self.songs_list) - 1
                    rand_indx = randint(0, size)
                    current_song = self.songs_list.pop(rand_indx)
                    self.copy_songs_list.append(current_song)

                    return current_song
                else:
                    size = len(self.songs_list) - 1
                    rand_indx = randint(0, size)
                    current_song = self.songs_list.pop(rand_indx)
                    self.copy_songs_list.append(current_song)

                    return current_song
            else:
                if len(self.songs_list) == 0:
                    self.songs_list = self.copy_songs_list[:]
                    self.copy_songs_list = []
                    current_song = self.songs_list.pop(0)
                    self.copy_songs_list.append(current_song)

                    return current_song
                else:
                    current_song = self.songs_list.pop(0)
                    self.copy_songs_list.append(current_song)

                    return current_song
        else:
            if self.shuffle is True:
                pass
            else:
                pass

    def pprint_playlist(self):

        table = [row.get_info() for row in self.songs_list]
        headers = ['Artist', 'Song', 'Length']

        print (tabulate(table, headers, tablefmt="orgtbl"))

    def save_playlist(self, filename):
        songs = {}

        filename = normalize_filename(filename)

        for song in self.songs_list:
            songs[str(song)] = song.__dict__

        with open(filename, "w") as outfile:
            outfile.write(json.dumps(songs))

    def load_playlist(self, filename):
        songs = {}

        with open(filename, "r") as infile:
            songs = json.load(infile)

        for song in songs.keys():
            self.add_song(Song(songs[song]['title'], songs[song][
                          'artist'], songs[song]['album'], songs[song]['length']))

    # from the solution
    # another possible realization of the json problem
    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.songs_list]
        }

        return data

    def save(self, indent=True):
        filename = self.name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p


def normalize_filename(filename):
    filename_list = filename.split(' ')
    result = '-'.join(filename_list)

    return result
