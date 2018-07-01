import regression
from numpy import *
import matplotlib.pyplot as plt
abX, abY = regression.loadDataSet('abalone.txt')
regression.stageWise(abX, abY, 0.001, 5000)

