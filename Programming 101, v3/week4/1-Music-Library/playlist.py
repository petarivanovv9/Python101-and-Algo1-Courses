from song import Song
from random import randint
from tabulate import tabulate


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

        sum_seconds = 0
        for song in self.songs_list:
            sum_seconds += song.get_length('seconds')

        sum_minutes = 0
        for song in self.songs_list:
            sum_minutes += song.get_length('minutes')

        return '{}:{}'.format(sum_minutes, sum_seconds)

    def artists(self):
        artists_histogram = {}
        artists = [x for x in self.songs_list.artist]

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
                    print ("HEREEEE")
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


# s = Song(title="Odin", artist="Manowar",
#          album="The Sons of Odin", length="3:44")

# p = Song(title="Choko", artist="Peshko",
#          album="Tdsdasd", length="2:99")

# k = Song(title="Bauuu", artist="Goshko",
#          album="Minsda", length="1:24")

# q = Song(title="jokooo", artist="Asan",
#          album="midsad", length="4:24")

# code_songs = Playlist("Code", True, True)

# code_songs.add_songs([s, p, k, q])

# code_songs.pprint_playlist()

# for song in code_songs.songs_list:
#     print (song.title)

# print (10 * '-')

# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
# print (code_songs.next_song())
