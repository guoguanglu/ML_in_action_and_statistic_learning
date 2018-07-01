import logRegres
from numpy import *
dataArr, labelMat = logRegres.loadDataSet()
weights = logRegres.stocGraAscent1(array(dataArr), labelMat)
logRegres.multiTest()
