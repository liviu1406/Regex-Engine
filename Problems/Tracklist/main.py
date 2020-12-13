# tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                       "On the Other Side": "Samara"},
#           "Cure": {"Disintegration": "Lovesong",
#                    "Wish": "Friday I'm in love"}}


def tracklist(**kwargs):
    for singer, dict_values in kwargs.items():
        print(singer)
        for album, song in dict_values.items():
            print(f'ALBUM: {album} TRACK: {song}')


# tracklist(**tracks)
