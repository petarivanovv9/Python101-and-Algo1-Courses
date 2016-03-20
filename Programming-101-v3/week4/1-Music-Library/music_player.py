from subprocess import Popen, PIPE
from music_crawler import MusicCrawler
from playlist import Playlist
from song import Song
import sys


def play(mp3Path):
    p = Popen(["mpg123", mp3Path], stdout=PIPE, stderr=PIPE)
    return p


def stop(process):
    process.kill()


print (10 * '-')
print ("Menu:")
print ("1. Generate songs from a directory and make a playlist.")
print ("2. PPrint playlist.")
print ("3. Get next song.")
print ("4. Play song.")
print ("5. Stop song.")
print ("0. Exit.")

while True:
    choice = input("Enter your choice: ")

    if choice is '1':
        directory = input("Type your directory: ")
        crawler = MusicCrawler(directory)
        new_playlist = crawler.generate_playlist()
    elif choice is '2':
        new_playlist.pprint_playlist()
    elif choice is '3':
        current_song = new_playlist.next_song()
        print ("The next song is: {}".format(current_song))
    elif choice is '4':
        bam = play(current_song.title + '.mp3')
    elif choice is '5':
        stop(bam)
    else:
        sys.exit()
