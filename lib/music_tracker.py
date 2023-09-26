class MusicTracker():
    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def list_songs(self):
        return self._songs
