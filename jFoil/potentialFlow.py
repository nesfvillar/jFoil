import numpy as np


def joukowskyTransform(z, b):
    return z + b**2 / z


def uniformCurrent(z, uInf, alpha):
    return uInf * z * np.exp(1j*alpha)


def dipole(z, uInf, a):
    return uInf * a**2 / z


def rotor(z, circulation):
    return -1j / 2*np.pi * circulation * np.log(z)
