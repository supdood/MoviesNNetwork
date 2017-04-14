import preprocess
import neural_network as net
import numpy as np
import time
import csv

NN = net.Neural_Network()
NN.W1 = np.loadtxt("saved_data/W1.txt")
NN.W2 = np.loadtxt("saved_data/W2.txt")
x = np.loadtxt("saved_data/x.txt")
y = np.loadtxt("saved_data/y.txt")

def train():
    time_taken = 0
    training_size = input("What size would you like the training set to be?: ")
    print()
    print("ok, building the training data ...")
        
    start = time.time()
    x, y, samples = preprocess.get_training_data(int(training_size))
    T = net.trainer(NN)
        
    print()
    print("Now training the network.")
    print()
    T.train(x, y)
    end = time.time()
    time_taken = end - start
        
    np.savetxt("saved_data/W1.txt", NN.W1)
    np.savetxt("saved_data/W2.txt", NN.W2)
    np.savetxt("saved_data/x.txt", x)
    np.savetxt("saved_data/y.txt", y)

    print(x)
    print()
    print(y)
    print()
    print('results:')
    print(NN.forward(x))
    print()
    print("It took " + str(time_taken) + " seconds to train the network.")
        
def predict(user_id, movie_id):
    input_x, actual_y, samples = preprocess.get_single_input(user_id, movie_id)
    
    prediction = NN.forward(input_x)
    print("Prediction: " + str(prediction))
    print("Actual: " + str(actual_y))
    difference = abs(prediction[0] - actual_y[0])
    print("Difference: " + str(difference))
    accuracy = 1-difference
    print("Accuracy: " + str(accuracy))
    
def predict_n_random(n):
    with open('results/random_result_sample.csv', 'w') as results_sample:
        writer = csv.writer(results_sample, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        start = time.time()
        writer.writerow(['userId', 'movieId', 'prediction', 'actualRating',
                         'difference', 'accuracy'])
   
        print("Preparing the input data for the network. This may take a while.")
        input_x, actual_y, samples = preprocess.get_training_data(n)
        print()
        print("Now feeding the input data into the network.")
        predictions = NN.forward(input_x)
        
        average = []
        print()
        print("Now writing the data to 'results/random_result_sample.csv'")
        for i in range(len(actual_y)):
            ids = samples[i][0].split()
            user_id = int(ids[0])
            movie_id = int(ids[1])
            
            prediction = predictions[i]
            actual = actual_y[i][0]
            difference = abs(prediction - actual)
            accuracy = 1 - difference
            
            row = [user_id, movie_id, prediction, actual, difference, accuracy]
            writer.writerow(row)
            average.append(accuracy)
        end = time.time()
        time_taken = end - start
        average = sum(average)/len(average)
        print()
        print("All " + str(n) + " predictions have now been written.")
        print()
        print("It took " + str(time_taken) + " seconds to makes the predictions and write them to the file.")
        print("The average accuracy is: " + str(average))
    