import math

def norm_value(V):
    """
    Returns a normalized value of a vector
    """
    sum = 0
    for x in V:
        sum += x*x
    return math.sqrt(sum)