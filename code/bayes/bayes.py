#encoding=utf-8
from numpy import *

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1] #1代表侮辱性文字，0代表正常言论
    return postingList, classVec

def createVocbList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def bagOfWords2VecMN(vocabList, inputSet):
    returnStr = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnStr[vocabList.index(word)] += 1
    return returnStr


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)    #避免与0项相乘，结果为0
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom               #change to log()避免结果下溢
    p0Vect = p0Num/p0Denom               #change to log()
    return p0Vect, p1Vect, pAbusive
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    list0Posts, listClasses =loadDataSet()
    myVocubList = createVocbList(list0Posts)
    trainMat = []
    for postindoc in list0Posts:
        trainMat.append(setOfWords2Vec(myVocubList, postindoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = setOfWords2Vec(myVocubList, testEntry)
    print testEntry,'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc =setOfWords2Vec(myVocubList, testEntry)
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)

def textPerse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []; classList = []; fullText = []
    for i in range(1, 26):
        wordList = textPerse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textPerse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocbList(docList)
    trainSet = range(50) ; testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainSet)))
        testSet.append(trainSet[randIndex])
        del(trainSet[randIndex])
    trainMat = [] ; trainClasses = []
    for docIndex in trainSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVec = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(wordVec, p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount)/len(testSet)

def calcMostFreq(vocabList, fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]
def localWords(feed1, feed0):
    import feedparser
    docList = []; classList = []; fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textPerse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        classList.append(1)
        fullText.extend(wordList)
        wordList = textPerse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        classList.append(0)
        fullText.extend(wordList)
    vocabList = createVocbList(docList)
    top30Words = calcMostFreq(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])
    trainingSet = range(2 * minLen); testSet = []
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(trainMat, trainClasses)
    errorCount = 0
    for docIndex in testSet:
        wordVec = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(wordVec, p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount)/len(testSet)
    return vocabList, p0V, p1V
def getTopWords(ny, sf):
    import operator
    vocabuList, p0V, p1V = localWords(ny, sf)
    topNY = []; topSF = []
    for i in range(len(p0V)):
        if p0V[i] > 0.01:
            topSF.append((vocabuList[i], p0V[i]))
        if p1V[i] > 0.01:
            topNY.append((vocabuList[i], p1V[i]))
    sortedSF =sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY"
    for item in sortedNY:
        print item[0]