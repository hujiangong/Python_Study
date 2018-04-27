from numpy import *
import matplotlib.pyplot as plt
import machinelearninginaction.Ch02.kNN as kNN  # 也可以import kNN 但是会有红色波浪线，看着很难受

def file2matrix(filename):
    """ 将文本记录转换为NumPy的解析程序"""
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    '''
    zeros(shape, dtype=None, order='C') 生成一个shape类型的矩阵，dtype为类型，order在内存中排列的方式（以C语言或Fortran语言方式排列），默认为C语言排列行优先；F代表列优先
    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
    array([(0, 0), (0, 0)]),
    >>> zeros((3,2))
    array([[ 0.  0.]
           [ 0.  0.]
           [ 0.  0.]]
    >>> zeros((3,))
    array([ 0.  0.  0.])
    '''
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

'''
创建一幅图便于直观化展示
fig = plt.figure() # 创建一幅图
ax=fig.add_subplot(111) # 349含义：将画布分成3行4列，图处于从左到右，从上到下的第九块
# x轴玩游戏占比，y轴每周冰激凌公升数，s(shape)形状，c(color)颜色
ax.scatter(x=datingDateMat[:,1],y=datingDateMat[:,2],s=15.0*array(datingLabels),c=15.0*array(datingLabels))
plt.show()
'''

def autoNorm(dataSet):
    """
    归一化特征值
    排除一些特征数本身数值就比较大，对结果造成影响
    下列采用数值归一化方法：newValue=（oldValue-min）/ （max-min）
    :param dataSet:
    :return: 归一化结果, 数值取值范围, 最小值
    """

    # TODO axis=1 将数据按行相加，axis=0, 将数据按列相加,感觉是从最外层的维度数量开始递增，待定？！
    minVals = dataSet.min(axis=0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDatSet = zeros(shape(dataSet))
    m = dataSet.shape[0]  # 行数
    normDatSet = dataSet - tile(minVals, (m, 1))
    normDatSet = normDatSet / tile(ranges, (m, 1))  # 这里的除法只是简单的对应同位置相除，矩阵除法有单独的函数
    return normDatSet, ranges, minVals

# autoNorm(datingDateMat)

def datingClassTest():
    """
    分类器针对约会网站的测试代码
    :return:
    """
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingData/datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]  # 行数
    numTestVecs = int(m * hoRatio)  # 确定测试的数据量
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = kNN.classify(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 4)
        print(classifierResult)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))

def classifyPerson():
    resultList = ["not at all", "in samll doses", "in large doses"]  # 可能的结果集
    percentTats = float(input("玩视频游戏所耗时间百分比？"))  # 输入
    ffMiles = float(input("每年获得的飞行常客里程数？"))
    iceCream = float(input("每周消费的冰淇淋公升数？"))
    datingDataMat, datingLabels = file2matrix('datingData/datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = kNN.classify((inArr - minVals) / ranges, normMat, datingLabels, 3)  # 先将输入进行归一化处理后输入
    print("你大概喜欢这个人的程度是", resultList[classifierResult - 1])

classifyPerson()
