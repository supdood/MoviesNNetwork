import csv
import preprocess

def mass_genre_lookup():
    with open('movielens_data/movies.csv', 'r', encoding='utf-8') as movies:
        reader = csv.reader(movies, delimiter=',')
        next(reader)
        
        lookup = [None] * 131263
        for row in reader:
            genres = row[2]
            genre_data = preprocess.genre_array(genres)
            lookup[int(row[0])] = genre_data
        return lookup
    