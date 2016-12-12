import csv

movies = [[i] for i in range(131263)]
with open ('movielens_data/ratings.csv', 'r') as ratings:
    reader = csv.reader(ratings, delimiter=',')
    with open('our_data/users_who_rated.csv', 'w') as users_who_rated:
        writer = csv.writer(users_who_rated, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        header = next(reader)
        
        for row in reader:
            movies[int(row[1])].append(float(row[0]))
        
        n_removed = 0
        
        for i in range(1, 131263):
            if len(movies[i-n_removed]) == 1:
                del movies[i-n_removed]
                n_removed += 1
            #else:
                #movies[i-n_removed][0] = movies[i-n_removed][0] + movies[i-n_removed][1]
                
        movies[0] = ['movieId']
        
        for row in movies:
            writer.writerow(row)
