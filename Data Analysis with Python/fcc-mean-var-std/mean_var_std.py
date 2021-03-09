import numpy as np

def calculate(l):
  
    if len(l) != 9:
        raise ValueError('List must contain nine numbers.')
    
    a = np.array(l).reshape((3,3))

    mean = [list(a.mean(axis=0)), list(a.mean(axis=1)), a.mean()]
    var = [list(a.var(axis=0)), list(a.var(axis=1)), a.var()]
    std = [list(a.std(axis=0)), list(a.std(axis=1)), a.std()]
    maximum = [list(a.max(axis=0)), list(a.max(axis=1)), a.max()]
    minimum = [list(a.min(axis=0)), list(a.min(axis=1)), a.min()]
    summation = [list(a.sum(axis=0)), list(a.sum(axis=1)), a.sum()]

    calculations = {'mean': mean,
    'variance': var,
    'standard deviation': std,
    'max': maximum,
    'min': minimum,
    'sum': summation}


    return calculations
