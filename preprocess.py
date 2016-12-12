import utils 
import random
import numpy as np

def get_training_data(movie_id, training_size):
    
    genre_lookup = utils.quick_genre_lookup()
    user_lookup = utils.quick_user_lookup()
    who_rated_lookup = utils.quick_who_rated()
    movie_average = utils.get_movie_average(movie_id)/5
    
    
    if(len(who_rated_lookup[movie_id]) < training_size):
        return "The training_size is too large."
    
    training_x = [0] * training_size
    training_y = [[] for i in range(training_size)]
  
    for i in range(training_size):
        random_user_id = float(random.choice(who_rated_lookup[movie_id]))
        random_user_id = "%g" % random_user_id
        random_user_id = int(random_user_id)
        random_user = user_lookup[random_user_id]
        print("start lookup " + str(i))
        training_y[i].append(utils.answer_lookup(random_user_id, movie_id)/5)      

        if random_user:
            genre_data = utils.relevant_genre_averages(random_user, genre_lookup[movie_id])
            user_average = utils.get_user_average(random_user_id)/5
            training_x[i] = [user_average, movie_average] + genre_data
        else:
            print('fail')
    return np.array(training_x), np.array(training_y)
