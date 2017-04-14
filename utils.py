import csv

def get_movie_average(i): 
    with open('our_data/average_user_ratings.csv', 'r', encoding='utf-8') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        
        i = str(i)
        
        for row in reader:
            if row[0] == i:
                return float(row[1])
        return False
            
def get_user_average(i): 
    with open('our_data/average_user_ratings.csv', 'r', encoding='utf-8') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        
        i = str(i)
        
        for row in reader:
            if row[0] == i:
                return float(row[1])
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
            "Children": 3,
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
        }.get(genre, -1)
        binary_genres[i] = 1    
    return binary_genres       

#Takes user data and a binary genre array for the corresponding movie.  Returns
#the average user rating for each of those genres in normalized form.
def relevant_genre_averages(user_data, genres):
    output = [0] * 18
    for i in range(18):
        if genres[i] == 1:
            output[i] = float(user_data[i+2])/5
    return output
        
    
def get_user_movie_data(u_id, m_id):
    u_avg = float(get_user_average(u_id))
    m_avg = float(get_movie_average(m_id))
    genres = genre_array(get_genres(m_id))
    
    user_movie_data = []    
    user_movie_data.append(u_avg)
    user_movie_data.append(m_avg)
    user_movie_data = user_movie_data + genres
    print(user_movie_data)   

def quick_genre_lookup():
    with open('movielens_data/movies.csv', 'r', encoding='utf-8') as movies:
        reader = csv.reader(movies, delimiter=',')
        next(reader)
        
        lookup = [None] * 131263
        for row in reader:
            genres = row[2]
            genre_data = genre_array(genres)
            lookup[int(row[0])] = genre_data
        return lookup
        
def quick_user_lookup():
    with open('our_data/average_user_ratings.csv', 'r', encoding='utf-8') as users:
        reader = csv.reader(users, delimiter=',')
        next(reader)
        
        lookup = [None] * 138494
        for row in reader:
            lookup[int(row[0])] = row
        return lookup        
    
def quick_who_rated():
    with open('our_data/users_who_rated.csv', 'r', encoding='utf-8') as movies:
        reader = csv.reader(movies, delimiter=',')
        next(reader)
        
        lookup = [None] * 131263
        for row in reader:
            index = int(row[0])
            del row[0]
            lookup[index] = row
        return lookup    
        
def user_movie_dict():
    with open('movielens_data/ratings.csv', 'r', encoding='utf-8') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        next(reader)
        dict = {}
        
        for row in reader:
            key = row[0] + " " + row[1]
            dict[key] = row[2]
        return dict
        
def average_genre_ratings(a):
    for i in range(len(a)):
        if (len(a[i]) > 0):
            a[i] = sum(a[i])/float(len(a[i]))
        else:
            a[i] = 0
    return a

def answer_lookup(user_id, movie_id):
    with open('movielens_data/ratings.csv', 'r', encoding='utf-8') as ratings:
        reader = csv.reader(ratings, delimiter=',')
        next(reader)
        
        for row in reader:
            if int(row[0]) == user_id and int(row[1]) == movie_id:
                return float(row[2])
        return False  
        
