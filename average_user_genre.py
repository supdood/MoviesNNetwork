import csv
import utils

with open ('movielens_data/ratings.csv', 'r') as ratings:
    reader = csv.reader(ratings, delimiter=',')
    with open('our_data/average_user_ratings.csv', 'w') as average_user:
        writer = csv.writer(average_user, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        header = next(reader)
                
        total_score = 0
        num_ratings = 1
        last_id = -1   
        lowest_index = -1
        
        writer.writerow(['userId', 'averageRating', 'Action', 'Adventure',
                         'Animation', 'Children', 'Comedy', 'Crime', 'Documentary',
                         'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
                         'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War',
                         'Western'])
        
        lookup = utils.quick_genre_lookup()     
        genre_ratings = [[] for i in range(18)]
        
        print("working...")
        
        for row in reader:  
            if last_id == row[0]:
                total_score += float(row[2])
                num_ratings += 1
                movie_id = row[1]
                movie_genres = lookup[int(movie_id)]
                for i in range(18):
                    if movie_genres[i] == 1:
                        genre_ratings[i].append(float(row[2]))
            else:
                if total_score != 0:
                    genre_avgs = utils.average_genre_ratings(genre_ratings)
                    row_data = [last_id, total_score/num_ratings] + genre_avgs
                    writer.writerow(row_data)
                last_id = row[0]
                total_score = float(row[2])
                num_ratings = 1
                genre_ratings = [[] for i in range(18)]
        
        genre_avgs = utils.average_genre_ratings(genre_ratings)
        row_data = [last_id, total_score/num_ratings] + genre_avgs
        writer.writerow(row_data)
        print("done")
