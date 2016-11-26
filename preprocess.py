import csv

def get_movie_average(i): 
    with open('our_data/average_user_ratings.csv', 'r', encoding='utf-8') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        
        i = str(i)
        
        for row in reader:
            if row[0] == i:
                return row[1]
        return False
            
def get_user_average(i): 
    with open('our_data/average_user_ratings.csv', 'r', encoding='utf-8') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        
        i = str(i)
        
        for row in reader:
            if row[0] == i:
                return row[1]
        return False
        
def get_genres(i):
    with open('movielens_data/movies.csv', 'r', encoding='utf-8') as movies:
        reader = csv.reader(movies, delimiter=',')
        
        i = str(i)
        
        for row in reader:
            if row[0] == i:
                return row[2]
        return False
        
#Takes a string of genres and returns an array representing the genres makeup
#in binary form.        
def genre_array(genres):
    genres = genres.split('|')
    binary_genres = [0] * 18
    
    for genre in genres:
        i = {
            "Action": 0,
            "Adventure": 1,
            "Animation": 2,
            "Children's": 3,
            "Comedy": 4,
            "Crime": 5,
            "Documentary": 6,
            "Drama": 7,
            "Fantasy": 8,
            "Film-Noir": 9,
            "Horror": 10,
            "Musical": 11,
            "Mystery": 12,
            "Romance": 13,
            "Sci-Fi": 14,
            "Thriller": 15,
            "War": 16,
            "Western": 17
        }.get(genre)
        binary_genres[i] = 1    
    print(binary_genres)
        
#print(get_movie_average(123))
#print(get_user_average(10))
print(get_genres(130384))
genre_array(get_genres(130384))
