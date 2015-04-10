class Song:

    def __init__(self, title='Unknown', artist='Unknown', album='Unknown', length='0'):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self):
        result = self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length
        return result

    def __hash__(self):
        to_hash_class = self.title + self.artist + self.album + self.length
        return hash(to_hash_class)

    def get_length(self, argument=''):
        length_list = self.length.split(':')[::-1]
        # print (length_list)
        if argument is 'seconds' and len(length_list) >= 0:
            return int(length_list[0])
        elif argument is 'minutes' and len(length_list) >= 1:
            return int(length_list[1])
        # elif argument is 'hours' and len(length_list) >= 2:
        #     return int(length_list[2])
        elif argument is '':
            # return str(self.length)
            return "{}".format(self.length)
        else:
            return 0

    def get_info(self):
        return [self.artist, self.title, self.length]

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}
