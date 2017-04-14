import utils 
import random
import numpy as np


print("building lookup resources")
genre_lookup = utils.quick_genre_lookup()
user_lookup = utils.quick_user_lookup()
rating_lookup = utils.user_movie_dict()


def get_training_data(training_size):
    
    training_x = []
    training_y = []

    samples = random.sample(rating_lookup.items(), training_size)
    
    for sample in samples:
        ids = sample[0].split()
        user_id = int(ids[0])
        movie_id = int(ids[1])
        
        movie_average = utils.get_movie_average(movie_id)/5
        random_user = user_lookup[user_id]
        genre_data = utils.relevant_genre_averages(random_user, genre_lookup[movie_id])
        user_average = float(random_user[1])/5
        
        training_x.append([user_average, movie_average] + genre_data)
        training_y.append([float(sample[1])/5])

    return np.array(training_x, dtype=float), np.array(training_y, dtype=float), samples

    
def get_single_input(user_id, movie_id):
    
    input_x = []
    output_y = []

    movie_average = utils.get_movie_average(movie_id)/5
    user = user_lookup[user_id]
    genre_data = utils.relevant_genre_averages(user, genre_lookup[movie_id])
    user_average = float(user[1])/5
    input_x.append([user_average, movie_average] + genre_data)

    
    key = str(user_id) + " " + str(movie_id)
    user_rating = float(rating_lookup[key])/5
    output_y.append(user_rating)
    
    return np.array(input_x), np.array(output_y)
    