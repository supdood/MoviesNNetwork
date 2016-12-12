import preprocess
import neural_network as net
import numpy as np

NN = net.Neural_Network()
x = None
y = None

def main():
    retrain = input("Would you like to retrain the Network? (y or n): ")
    if retrain == "y":
        print("ok")
        movie_id = input("What is the id of the movie you'd like to train for?: ")
        training_size = input("What size would you like the training set to be?: ")
        
        x, y = preprocess.get_training_data(int(movie_id), int(training_size))
        T = net.trainer(NN)
        T.train(x, y)
        
        np.savetxt("saved_data/W1.txt", NN.W1)
        np.savetxt("saved_data/W2.txt", NN.W2)
        np.savetxt("saved_data/x.txt", x)
        np.savetxt("saved_data/y.txt", y)
        
    else:
        print("ok")
        NN.W1 = np.loadtxt("saved_data/W1.txt")
        NN.W2 = np.loadtxt("saved_data/W2.txt")
        x = np.loadtxt("saved_data/x.txt")
        y = np.loadtxt("saved_data/y.txt")

    print(x)
    print()
    print(y)
    print()
    print('results:')
    print(NN.forward(x))
    