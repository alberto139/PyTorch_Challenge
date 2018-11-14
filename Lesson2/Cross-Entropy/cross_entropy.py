import numpy as np

# My solution
def cross_entropy(Y, P):
    
    sum = 0
    for i in range(len(Y)):
        sum += Y[i]*np.log(P[i]) + (1 - Y[i])*np.log(1-P[i])
        
    return -sum

# Udacity provided solution
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))