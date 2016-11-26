import csv

movies = [[i, []] for i in range(131263)]
with open ('movielens_data/ratings.csv', 'r') as ratings:
    reader = csv.reader(ratings, delimiter=',')
    with open('our_data/average_movie_ratings.csv', 'w') as movie_averages:
        writer = csv.writer(movie_averages, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        header = next(reader)
        
        for row in reader:
            movies[int(row[1])][1].append(float(row[2]))
        
        n_removed = 0
        
        for i in range(1, 131263):
            if not movies[i-n_removed][1]:
                del movies[i-n_removed]
                n_removed += 1
            else:
                movies[i-n_removed][1] = sum(movies[i-n_removed][1])/len(movies[i-n_removed][1])
                
        movies[0] = ['movieId', 'averageRating']
        
        for row in movies:
            writer.writerow(row)
