import numpy as np
from numpy import double

G = 1  # Gravitational constant
m_1: double = 0.0  # (user input) Mass of gravitational body
m_2: double = 0.0  # (user input) Mass or small object
r_2_1 = np.array([1, 1, 1])  # (User input) Initial position relative to gravitational body
v_i = np.array([0, 0, 0])  # (User input) Initial velocity


# reference (0,0,0) is set at position of big mass
# return array representing positions of the small mass
def simulateOrbital(v_i, pos_i, m_o, m_b):
    # compute first point, termination range is equal to distance from first to starting
    # while
    #    if

    return


# p represents range
def isInTermRange(r, v):
    # v[]

    return


# returns magnitude of vector v
def mag(r):
    return np.sqrt(r[0] * r[0] + r[1] * r[1] + r[2] * r[2])


# Find unit vector of a vector. (Needed for finding the unit vector of the position)
def findUnitVector(r):
    return r / mag(r)


# Find the resulting force on our object on which we want to compute the trajectory
def findForce(r_2_1):
    F = np.zeros(3)
    F = -G((m_1 * m_2) / (mag(r_2_1) ** 2)) * findUnitVector(r_2_1)
    return F
