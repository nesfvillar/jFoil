import numpy as np
import matplotlib.pyplot as plt

class Airfoil:
    def __init__(self, foil):
        self.foil = foil

    def plotFoil(self, title='', grid=False):
        """  plotFoil """
        plt.plot(np.real(self.foil), np.imag(self.foil))
        plt.title(title)
        plt.axis("scaled")
        if grid:
            plt.grid()
        plt.show()

    def saveFoil(self, filename='foil.csv'):
        """ saveFoil """
        np.savetxt(filename, self.foil, fmt='%f;%f', header='x;y', comments='')


class JFoil(Airfoil):
    """ Joukowsky foil creator.

    Parameters:

    a - Radius of the pre-transformation cilinder. Approximately 1/4 of the final chord length.

    relThickness - Proportional to the thickness of the airfoil. Must be between 0 and 1. For airfoils, it is generally close to 0.9.

    beta - Curvature of the foil in degrees.

    [n] - number of samples that make the foil. Default 100. """

    def __init__(self, a, relThickness, beta, n=100):
        assert relThickness > 0 and relThickness < 1

        self.a = a
        self.relThickness = relThickness
        self.beta = np.deg2rad(beta)

        theta = np.linspace(0, 2*np.pi, n)
        cilinder = self.a * (np.exp(1j*theta) - self.relThickness + np.exp(1j*self.beta))

        super().__init__(self._joukowskyTransform(cilinder, self.a * self.relThickness))

    def _joukowskyTransform(self, z, b):
        return z + b**2 / z