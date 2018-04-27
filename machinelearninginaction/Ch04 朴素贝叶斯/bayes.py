from numpy import *

def loadDataSet():
    postingList = [['my', 'my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is 侮辱性文字, 0 正常言论
    return postingList, classVec

def createVocabList(dataSet):
    """
    包含所有文档的不重复词列表
    :param dataSet:
    :return:
    """
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # |用于求两个集合的并集
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    """
    判断inputSet的数据是否在vocabList中并且位置在哪
    :param vocabList:
    :param inputSet:
    :return:
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    """
    朴素贝叶斯分类器训练函数
    :param trainMatrix: 文档矩阵
    :param trainCategory: 每篇文档类别标签所构成的向量
    :return:p0Vect 正常言论句子中的每一个单词出现的次数占总正常言论单词次数的比例
    :return:p1Vect 侮辱言论句子中的每一个单词出现的次数占总侮辱言论单词次数的比例
    :return:pAbusive 侮辱言论句子占所有句子的比例
    """
    numTrainDocs = len(trainMatrix)  # 训练集的数量6
    numWords = len(trainMatrix[0])  #
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 计算侮辱性文档的概率(因为trainCategory=1时是侮辱性)
    # p0Num = zeros(numWords) # 区别之一：zeros是0，ones是1
    # p1Num = zeros(numWords)
    # p1Denom = 0.0
    # p0Denom = 0.0
    # 当计算多个概率的乘积时，如果某一个的概率为0，那么乘出来的也是0，为了降低这种影响，将所有词
    # 出现数初始化为1，分母初始化为2
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p1Denom = 2.0
    p0Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]  # 将trainMatrix中的每一个list累加
            p1Denom += sum(trainMatrix[i])  # 这里也可以在for循环完成后sum(p1Num)
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 当很多很小的数相乘时，可能会造成下溢出得不到正确答案或者乘积为0。这时可以用对数。ln(a*b)=ln(a)+ln(b)，不会有任何损失。而且曲线在相同区域内同时增加或者减少，并且在相同点上取到极值
    # p1Vect = p1Num / p1Denom # 消极句子中的每一个单词出现的次数占总消极句子中单词数的次数
    # p0Vect = p0Num / p0Denom
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    """
    朴素贝叶斯分类函数
    :param vec2Classify:
    :param p0Vec:
    :param p1Vec:
    :param pClass1:
    :return:
    """
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # sum(每一个词的出现次数*在侮辱组中出现的概率)+log(侮辱句子的概率)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    """
    便利函数，组合所有函数，节省时间
    :return:
    """
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry=['stupid','garbage']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))

# listOPosts, listClasses = loadDataSet()
# myVocabList = createVocabList(listOPosts)  # 将listOPosts去重成set集合
# trainMat = []
# for postinDoc in listOPosts:
#     trainMat.append(setOfWords2Vec(myVocabList, postinDoc))  # myVocabList中postinDoc出现的位置
# p0V, p1C, pAb = trainNB0(trainMat, listClasses)
# print(p0V)
testingNB()
