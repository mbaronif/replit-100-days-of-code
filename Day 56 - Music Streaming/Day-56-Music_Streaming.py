import csv, os

topSongs = []

# Reads the CSV file.
with open("/Users/marianabaronifontana/Projects/replit-100-days-of-code/Day 56 - Music Streaming/TopSongs.csv", "r") as file:
    # Reads the CSV file using the csv module.
    f = csv.DictReader(file)
    for row in f:
        # Adds the song to the list.
        topSongs.append(row)


# Displays the full ranking of the songs.
def fullRanking():
    for song in topSongs:
        print(song)
    print()

fullRanking()