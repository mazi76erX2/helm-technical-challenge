from .song import Song


class TestSong:
    def test_non_repeating_playlist(self):
        first = Song("Hello")
        second = Song("Eye of the tiger")
        third = Song("Bohemian Rhapsody")
        first.next_song(second)
        second.next_song(third)
        assert not first.is_repeating_playlist()

    def test_repeating_playlist_multiple_songs(self):
        first = Song("Hello")
        second = Song("Eye of the tiger")
        third = Song("Bohemian Rhapsody")
        fourth = Song("Hotel California")
        first.next_song(second)
        second.next_song(third)
        third.next_song(fourth)
        fourth.next_song(first)
        assert first.is_repeating_playlist()

    def test_repeating_playlist_two_songs(self):
        first = Song("Hello")
        second = Song("Eye of the tiger")
        first.next_song(second)
        second.next_song(first)
        assert first.is_repeating_playlist()

    def test_empty_playlist(self):
        first = Song("Hello")
        assert not first.is_repeating_playlist()

    def test_single_song_playlist(self):
        # Test case for a playlist with only one song
        song = Song("Hello")
        assert not song.is_repeating_playlist()

    def test_repeating_playlist_same_song(self):
        # Test case for a playlist with the same song repeating
        first = Song("Hello")
        first.next_song(first)
        assert first.is_repeating_playlist()

    def test_repeating_playlist_multiple_loops(self):
        # Test case for a playlist with multiple loops
        first = Song("Hello")
        second = Song("Eye of the tiger")
        third = Song("Bohemian Rhapsody")
        first.next_song(second)
        second.next_song(third)
        third.next_song(first)
        assert first.is_repeating_playlist()
