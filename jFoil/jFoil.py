import numpy as np
import matplotlib.pyplot as plt


class jFoil:
    """ Jowkousky foil creator.

    Parameters:

    a - Radius of the pre-transformation cilinder. Approximately 1/4 of the final chord length.

    bOverA - Proportional to the thickness of the airfoil. Must be between 0 and 1. For airfoils, it is generally close to 0.9.

    beta - Curvature of the foil in degrees.

    [n] - number of samples that make the foil. Default 50. """

    def __init__(self, a, bOverA, beta, n=50):
        if bOverA < 0 or bOverA > 1:
            raise ValueError(
                "Bad value of airfoil thickness (bOverA must be between 0 and 1)")

        self.a = a
        self.bOverA = bOverA
        self.beta = np.deg2rad(beta)

        self.theta = np.linspace(0, 2*np.pi, n)
        self.cilinder = self.a * (np.exp(1j*self.theta) - self.bOverA +
                                  np.exp(1j*self.beta))

        self.foil = joukowskyTransform(self.cilinder, self.a * self.bOverA)

    def plotFoil(self, title='', grid=False):
        plt.plot(np.real(self.foil), np.imag(self.foil))
        plt.title(title)
        plt.axis("scaled")
        if grid:
            plt.grid()
        plt.show()

    def saveFoil(self, filename='foil.csv'):
        np.savetxt(filename, self.foil, fmt='%f;%f', header='x;y', comments='')

    def currentLines(self, alpha=0):
        # TODO add current lines plot
        return

    def plotcL(self, minAlpha=-5, maxAlpha=5, n=50):
        # TODO plot cL as a function of alpha
        minAlpha = np.deg2rad(minAlpha)
        maxAlpha = np.deg2rad(maxAlpha)

        alpha = np.linspace(minAlpha, maxAlpha, n)
        cL = 2*np.pi * np.sin(alpha + self.beta)

        plt.plot(np.rad2deg(alpha), cL)
        plt.xlabel("alpha (°)")
        plt.ylabel("cL")
        plt.grid()
        plt.show()


def joukowskyTransform(z, b):
    return z + b**2 / z


def main():
    # TODO add input to use the command line to create airfoils
    return


if __name__ == '__main__':
    main()
