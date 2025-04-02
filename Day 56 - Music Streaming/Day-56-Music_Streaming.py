import csv, os

# Replaces the file path with a shorter variable name.
file_path = "/Users/marianabaronifontana/Projects/replit-100-days-of-code/Day 56 - Music Streaming/TopSongs.csv"

topSongs = []

# Reads the CSV file.
with open(file_path, "r") as file:
    # Reads the CSV file using the csv module.
    reader = csv.DictReader(file)
    for row in reader:
        # Adds the song to the list.
        #topSongs.append(f"{row['Position']} - {row['Artist']} | {row['Title']} | {row['Year']} | {row['Total']}")
        # It should create a new location for each artist, but it didn't.
        artist_path = os.path.join("/Users/marianabaronifontana/Projects/replit-100-days-of-code/Day 56 - Music Streaming/", row['Artist'])
        print(artist_path)

# Displays the full ranking of the songs.
def fullRanking():
    for song in topSongs:
        print(song)
    print()

#This is only for testing purposes.
#fullRanking()

# Creates a directory for each artist.