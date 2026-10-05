# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
music_types = {
    "music1": ["pop1", "pop2", "pop3"],
    "music2": ["rock1", "rock2", "rock3"],
    "music3": ["jazz1", "jazz2", "jazz3"],
    "music4": ["classical1", "classical2", "classical3"]
}
# (keys are artist names, values are lists of album names)
artists = {
    "artist1": ["album1", "album2", "album3"],
    "artist2": ["album4", "album5", "album6"],
    "artist4": ["album7", "album8", "album9"],
    "artist3": ["album10", "album11", "album12"]
}


# Pretty-print the data structure
pprint(artists)

# Display details of one album recorded by a specific artist
