import numpy as np

def plasma_concentration(A, p_inf, time, tau):
    return (A * np.exp(-time/tau)) + p_inf