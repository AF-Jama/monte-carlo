# following will estimate pi using monte carlo method
# monte carlo method involves generating random x and y coordinates from (0,1(inclusive)) and checking if the coordinates are valid using x^2+y^2 <1 then they are classified as hits and if not they are are classified as misses
# misses and hits will be plotted using matplot lib
import random
from matplotlib import colors
import matplotlib.pyplot as plt 
import numpy as np

def monte_pi(num_of_plots = 100):
    plt.title("Approximation of pi using monte carlo method")   
    hits = 0
    misses  = 0
    hits_x = []
    hits_y = []
    misses_x = []
    misses_y = []
    #takes in one argument which is the number of points needed to estimate pi. ie: 100,1000,10000 etc. by defualt it is set to 100 points
    for i in range(num_of_plots):
        x = round(random.random(),2) #returns random floating point between 0.0 and 1.0 for x axis
        y = round(random.random(),2) #returns random floating point between 0.0 and 1.0 for y axis
        calc = round((x**2) + (y**2),2) # compared to x^2+y^2<1
        if calc<=1:
            hits+=1
            #plot hit in red
            hits_x.append(x)
            hits_y.append(y)
        else:
            misses+=1
            #plot miss in blue
            misses_x.append(x)
            misses_y.append(y)


        # print("Total number of points tried:" + str(i))
        # print("Total Number of hits:" + str(hits))
        # print("Total Number of misses:" + str(misses))
        estimation = hits/(i+1) # this is an estimation of pi/4
        # to get an estimation of pi estimation is multiplied by 4 
        estimation = round(estimation*4,3)
        print("Pi estimation:" + str(estimation))

    plt.title("Approximation of pi using monte carlo method")
    plt.scatter(x = hits_x,y = hits_y, c = 'r')
    plt.scatter(x = misses_x,y = misses_y, c ='b')
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.show()

monte_pi(100000)


