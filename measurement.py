import numpy as np

def measure(state):
    """Measures the qubit state in the z-basis. Returns the measurement outcome (1 or -1)"""
    prob_1 = abs(state[0])**2 #calculates probability of measurement outcome of one
    comparison_for_prob=np.random.rand()
    #compares a random number to the probability of outcome of one. Iff number is smaller, return one.
    if prob_1>comparison_for_prob: 
        outcome=1
    else:
        outcome=-1
    return(outcome)