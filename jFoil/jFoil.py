import numpy as np
import matplotlib.pyplot as plt


class jFoil:
    """ Jowkousky foil creator and plotting.

    Parameters:

    a - Radius of the pre-transformation cilinder. Approximately 1/4 of the final chord length.

    bOverA - Proportional to the thickness of the airfoil. Must be between 0 and 1. For airfoils, it is generally close to 0.9.

    beta - Curvature of the foil in degrees.

    [alpha] - Angle of attack in degrees. Default 0.

    [n] - number of samples that make the foil. Default 50. """

    def __init__(self, a, bOverA, beta, alpha=0, n=50):
        if bOverA < 0 or bOverA > 1:
            raise ValueError(
                "Bad value of airfoil thickness (bOverA must be between 0 and 1)")

        self.a = a
        self.bOverA = bOverA
        self.alpha = np.deg2rad(alpha)
        self.beta = np.deg2rad(beta)

        self.theta = np.linspace(0, 2*np.pi, n)
        self.cilinder = self.a * (np.exp(1j*self.theta) - self.bOverA +
                                  np.exp(1j*self.beta))

        self.foil = joukowskyTransform(
            self.cilinder, self.a * self.bOverA) * np.exp(1j*self.alpha)

    def plotFoil(self, title='', grid=False):
        plt.plot(np.real(self.foil), np.imag(self.foil))
        plt.title(title)
        plt.axis("scaled")
        if grid:
            plt.grid()
        plt.show()

    def saveFoil(self, filename='foil.csv'):
        extension = filename.split(sep='.')[-1]
        if extension == 'csv':
            np.savetxt(filename, self.foil, fmt='%f;%f',
                       header='x;y', comments='')
        else:
            np.savetxt(filename, self.foil, fmt='%f;%f')


def joukowskyTransform(z, b):
    return z + b**2 / z


# TODO add input to use the command line to create airfoils
def main():
    foil = jFoil(1, 0.85, 6)
    foil.plotFoil()


if __name__ == '__main__':
    main()
