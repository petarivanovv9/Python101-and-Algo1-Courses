class Song:

    def __init__(self, title='Unknown', artist='Unknown', album='Unknown', length='0', path=''):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.path = ''

    def __str__(self):
        return "{} - {} from {} - {}"\
            .format(self.artist, self.title, self.album, self.length)

    # def __eq__(self, other):
    #     result = self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length
    #     return result

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def get_length(self, argument=''):
        length_list = self.length.split(':')[::-1]
        seconds = 0
        minutes = 0
        hours = 0

        if len(length_list) == 3:
            seconds = int(length_list[0])
            minutes = int(length_list[1])
            hours = int(length_list[2])
        elif len(length_list) == 2:
            seconds = int(length_list[0])
            minutes = int(length_list[1])
        else:
            raise ValueError(
                "Length not proper format: {}".format(self.length))

        if argument is 'seconds':
            return seconds + 60 * minutes + 60 * 60 * hours
        if argument is 'minutes':
            return minutes + 60 * hours
        if argument is 'hours':
            return hours

        # if argument is 'seconds' and len(length_list) >= 0:
        #     return int(length_list[0])
        # elif argument is 'minutes' and len(length_list) >= 1:
        #     return int(length_list[1])
        # elif argument is 'hours' and len(length_list) >= 2:
        # return int(length_list[2])
        # elif argument is '':
        # return str(self.length)
        #     return "{}".format(self.length)
        # else:
        #     return 0

    def get_info(self):
        return [self.artist, self.title, self.length]

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}
