class Song:
    """ A class to represent a song
    Attributes: 
    title (str): The title of the song
    artist (Artist): An artist object representing the song's creator
    duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method
        Args:
        title (str): Initializes the 'title' attribute
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


help(Song)
# help(Song.__init__)
help(Song.__init__.__doc__)

Song.__init__.__doc__ = """  Song init method       

        Args:
        title (str): Initializes the 'title' attribute
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. Will default to zero if not specified.
        """