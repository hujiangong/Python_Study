from math import log
import operator

def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ["no surfacing", "flippers"]
    '''
    dataSet = [
        [1, 1, 0, 'yes'],
        [1, 1, 1, 'no'],
        [1, 0, 1, 'no'],
        [0, 1, 0, 'yes'],
        [0, 1, 1, 'no']
    ]
    labels = ["surfacing", "flippers", "hehe"]
    '''
    return dataSet, labels

def calcShannonEnt(dataSet):
    """
    计算给定数据集的香农熵
    :param dataSet:
    :return:
    """
    numEntries = len(dataSet)
    labelsCounts = {}
    for featVec in dataSet:
        currentLabels = featVec[-1]
        if currentLabels not in labelsCounts.keys():
            labelsCounts[currentLabels] = 0
        labelsCounts[currentLabels] += 1
    shannonEnt = 0.0
    for key in labelsCounts:
        prob = float(labelsCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)  # 以2为底
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    """
    按照给定特征划分数据集
    :param dataSet:
    :param axis: 指定列，也就是属性
    :param value: 属性的某个值
    :return: 都属性为某个值时的数据
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
            '''
            a=[1,2,3]
            b=[4,5,6]
            a.append(b) #[1,2,3,[4,5,6]]
            a.extend(b) #[1,2,3,4,5,6]
            '''
    # print("retDataSet:" + str(retDataSet))
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 0是指第一行
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]  # 取每一列的值
        uniqueVals = set(featList)  # 转换成set类型，去重
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            '''
            subDataSet
            [[1, 'no'], [1, 'no']]
            [[1, 'yes'], [1, 'yes'], [0, 'no']]
            '''
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  # 信息增益=信息熵-条件熵
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    """
    创建树
    :param dataSet:
    :param labels:
    :return:
    """
    classList = [example[-1] for example in dataSet]  # 结果集
    if classList.count(classList[0]) == len(classList):  # 类别完全相同则停止划分
        return classList[0]
    if len(dataSet[0]) == 1:  # 遍历完所有特征时返回出现次数最多的类别
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]  # 取最合适的属性
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])  # 删除已用掉的属性
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]  # 取剩下的所有属性
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)  # 递归
    return myTree

myDat, labels = createDataSet()
result = createTree(myDat, labels)
# {'surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
# print(result)
