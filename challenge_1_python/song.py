class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        visited = set()
        current = self

        while current is not None:
            if current in visited:
                return True

            visited.add(current)
            current = current.next

        return False
