"""
This func is to plot ROC curve of predictions. First, you need a file consisting of prediction results,
and a label file. However, the way I generate test set is one positive sample and one unlabeled sample,
so I decide to create the label vector without that file.
"""
from numpy import *

__author__ = 'Liu Can'

def loadfile(predictFile):
    fp1 = open(predictFile)
    resultVec, labelVec = [], []
    i = 0
    for line in fp1.readlines():
        tmp = line.strip()
        resultVec.append(float(tmp))
        if i%2 == 0:
            labelVec.append(1)
        else:
            labelVec.append(-1)
        i += 1
    return array(resultVec), array(labelVec)  #return two np.array type objects

def plotROC(resArr, labelArr):
    import matplotlib.pyplot as plt
    curPoint = (1.0, 1.0)
    ySum = 0.0
    numOfPosSample = sum(array(labelArr) == 1)
    numOfUnlabeledSam = len(labelArr) - numOfPosSample
    xStep = 1.0 / numOfUnlabeledSam
    yStep = 1.0 / numOfPosSample
    fig = plt.figure(dpi=100)
    fig.clf()
    ax = plt.subplot(111)       #subplot belongs to plt, not a method of figure object
    sortedIndices = resArr.argsort()
    for index in sortedIndices.tolist():
        if labelArr[index] == 1:
            deltaX = 0
            deltaY = yStep
        else:
            deltaX = xStep
            deltaY = 0
            ySum += curPoint[1]
        ax.plot([curPoint[0], curPoint[0]-deltaX], [curPoint[1], curPoint[1]-deltaY], c='b')
        curPoint = (curPoint[0]-deltaX, curPoint[0]-deltaY)
    ax.plot([0,1], [0,1],'p--')    #This line aims to draw a diagonal from (0,0) to (1,1)
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC curve')
    ax.axis([0,1, 0, 1])
    plt.show()
    print 'the AUC value is ', ySum * xStep

if __name__ == "__main__":
    resArr=array([1,2,3,4,5,6,7,8,9,10])
    labelArr = [0,0,0,1,0,1,0,1,1,1]
    plotROC(resArr, labelArr)
