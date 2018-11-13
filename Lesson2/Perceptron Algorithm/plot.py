import numpy as np
import csv
import matplotlib.pyplot as plt
from perceptron import * 


def main():
    
    data_points = []# points and their labels
    xs = []
    ys = []

    labels_colors = []
    X = []
    y = []

    lines = []

    with open('data.csv') as data:
        reader = csv.reader(data)
        for row in reader:  
            # Reading in this format beacuse it easier for plotting
            data_points.append(((float(row[0]), float(row[1])), row[2]))
            xs.append(float(row[0]))
            ys.append(float(row[1]))

            # Reading in this format beacuse it easier for maths
            X.append([float(row[0]), float(row[1])])
            y.append(float(row[2]))

    X = np.array(X)
    y = np.array(y)

    lines = (trainPerceptronAlgorithm(np.array(X), np.array(y)))

   # Convert labels to colors for pyplot
    colors = {0 : 'b',
              1 : 'r'}
    c = [colors[label] for label in y]

    
    # Plot data points
    x = [-0.5, 0.0, 0.5, 1.0, 1.5]

    for line in lines[0]:
        #plt.plot(line[0]*x, line[1])
        plt.scatter(xs, ys, c=c)
        plt.ylim([-.5,1.5])
        plt.xlim([-.5,1.5])
        
        y = lambda x: line[0] * x + line[1]
        plt.plot(x, y(x),'b--',label='Line from perceptron implementation.')
    plt.show()

if __name__ == '__main__':
    main()