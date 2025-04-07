import csv, os

# Replaces the pathes of the parent folder and the file with a shorter variable name.
parent_path = ".../Day 56 - Music Streaming/"
file_path = os.path.join(parent_path, "TopSongs.csv")

# Reads the CSV file using the csv module.
with open(file_path) as file:
    reader = csv.DictReader(file)

    # Reads each line of the CSV file.
    for row in reader:
        artist = row['Artist']
        title = row['Title']

        # Creates a folder for each artist.
        artist_path = os.path.join(parent_path, artist)

        file_dir = os.listdir(parent_path)
       # Checks if the file is empty.
        
        # Checks if the artist folder already exists.
        # If not, it creates a new folder.
        if artist not in file_dir:
            os.mkdir(artist_path)
        
        # Creates a file for each song in the respective artist folder.
        path = os.path.join(artist_path, title)
        f = open(path, "w")
        f.close()