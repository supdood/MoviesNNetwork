import csv

def get_movie_average(i): 
    with open('movielens_data/ratings.csv', 'r') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        
        i = str(i)
        ratings = []
        
        for row in reader:
            if row[1] == i:
                ratings.append(float(row[2]))
        if len(ratings) > 0:
            return sum(ratings)/len(ratings)
        else:
            return False
            
def get_user_average(i): 
    with open('our_data/average_user_ratings.csv', 'r') as ratings:
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
        
def genre_array(genres):
    genres = genres.split('|')
        
print(get_movie_average(1))
#print(get_user_average(10))
#rint(get_genres(130384).split('|'))