import adaboost
from numpy import *
#datMat, classLabels = adaboost.loadSimpleData()
datMat, classLabels = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray, aggClassEst = adaboost.adaBoostTrainDS(datMat, classLabels, 10)
adaboost.plotROC(aggClassEst.T, classLabels)


