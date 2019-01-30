import numpy as np

def measure(state):
    """Measures the qubit state in the z-basis. Returns the measurement outcome (1 or -1)"""
    prob_1 = abs(state[1])**2
    comparison_for_prob=np.random.rand()
    if prob_1<comparison_for_prob:
        outcome=1
    else:
        outcome=-1
    return(outcome)