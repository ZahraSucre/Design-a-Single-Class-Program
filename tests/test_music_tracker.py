from lib.music_tracker import MusicTracker

"""
Initially, there are no songs
"""
def test_initially_has_no_songs():
    tracker = MusicTracker()
    assert tracker.list_songs() == []

"""
When we add a song
It is reflected in the list of songs
"""
def test_add_song_reflected_in_songs():
    tracker = MusicTracker()
    tracker.add("Stayin Alive")
    assert tracker.list_songs() == ["Stayin Alive"]

"""
When we add multiple songs
They all reflected in the list of songs
"""
def test_add_multiple_songs():
    tracker = MusicTracker()
    tracker.add("Stayin Alive")
    tracker.add("Yay")
    tracker.add("Guli Mata")
    assert tracker.list_songs() == ["Stayin Alive", "Yay", "Guli Mata"]
