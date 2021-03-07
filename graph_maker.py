#Program that makes a graph based on the data from a .txt-file

import matplotlib.pyplot as plt
import numpy as np

def make_array_from_txt(filename):

    array = []
    file1 = open(filename, "a")

    while file1.readline():
        line = file1.readline()
        array.append(line)

    file1.close()
    return array

if __name__ == "__main__":

    print("What file do you want to plot?")
    filename = input()

    x = np.linspace(0, 10)
    y = make_array_from_txt(filename)
    
    plt.plot(x, y)
    plt.xlabel("Time")
    plt.ylabel("Distance")
    plt.title("Distance measured from file - ", filename)
    plt.show()