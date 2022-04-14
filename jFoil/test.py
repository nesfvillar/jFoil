import unittest as ut
from jFoil import *


class JFoilTest(ut.TestCase):

    def setUp(self):
        self.foil = jFoil(1, 0.9, 5)

    def testPlotFoil(self):
        pass
        # self.foil.plotFoil()

    def testSaveFoil(self):
        pass

    def testPlotCl(self):
        pass
        # self.foil.plotCl()


if __name__ == '__main__':
    ut.main()
