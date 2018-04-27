from numpy import *
import operator

# 准备数据
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    # labels = ['B', 'B', 'A', 'A']
    return group, labels

# k-近邻算法
def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 行数
    # 因为输入的参数inX和dataSet列数一样，所以tile(inX,(dataSetSize,1))相当于创建了一个和dataSet行数和列数一样的数组，
    # 和dataSet相减即得到未知数据和每一个dataSet数据的差值
    '''
    tile(A,reps) reps的数字从后往前分别对应A的第N维度的重复次数
    a = array([0, 1, 2])
    print(tile(a, (2, 3, 2)))
    [[[0 1 2 0 1 2]
      [0 1 2 0 1 2]
      [0 1 2 0 1 2]]
     [[0 1 2 0 1 2]
      [0 1 2 0 1 2]
      [0 1 2 0 1 2]]]
    '''
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqdistances = sqDiffMat.sum(axis=1)  # axis=1 将数据按行相加，axis=0, 将数据按列相加
    distances = sqdistances ** 0.5
    '''
    argsort() 不是平时理解的排序，是给出从小到大的数位于第几个
    [ 1.48660687  1.41421356  0.          0.1       ]
    [2 3 1 0]
    '''
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        # dict.get(key, default=None) 函数返回指定键的值，如果值不在字典中返回默认值
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    '''
    对给定的List L进行排序，
    方法1.用List的成员函数sort进行排序，在本地进行排序，不返回副本
    方法2.用built-in函数sorted进行排序（从2.4开始），返回副本，原始输入不变
    sorted(iterable, cmp=None, key=None, reverse=False)
    iterable：是可迭代类型;
    cmp：用于比较的函数，比较什么由key决定;
    key：用列表元素的某个属性或函数进行作为关键字，有默认值，迭代集合中的一项;
    reverse：排序规则. reverse = True  降序 或者 reverse = False 升序，有默认值。
    返回值：是一个经过排序的可迭代类型，与iterable一样。 本例中为 [('B', 2), ('A', 1)]
    '''
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
classify([0, 0], group, labels, 3)
