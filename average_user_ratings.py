import csv

with open ('movielens_data/ratings.csv', 'r') as ratings:
    reader = csv.reader(ratings, delimiter=',')
    with open('our_data/average_user_ratings.csv', 'w') as average_user:
        writer = csv.writer(average_user, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        header = next(reader)
                
        total_score = 0
        num_ratings = 1
        last_id = -1
        
        lowest_index = -1
        
        writer.writerow(['userId', 'averageRating'])
        
        for row in reader:
            if last_id == row[0]:
                total_score += float(row[2])
                num_ratings += 1
            else:
                if total_score != 0:
                    writer.writerow([last_id, total_score/num_ratings])
                last_id = row[0]
                total_score = float(row[2])
                num_ratings = 1
        writer.writerow([last_id, total_score/num_ratings])
        
