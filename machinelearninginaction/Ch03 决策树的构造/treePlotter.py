import matplotlib.pyplot as plt
import trees

'''
pyplot和pylab的异同：
两个都是matplotlib的模块。
pyplot在matplotlib的子模块中，仅用来画图
pylab可直接引用，集成了pyplot和numpy的大部分方法，可用于交互式
'''
# 增加下两行即可在图形中显示中文
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    # 图的各种格式
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords="axes fraction", xytext=centerPt, textcoords="axes fraction",
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot(inTree):
    fig = plt.figure(1, facecolor="white")  # facecolor背景色
    fig.clf()
    axprops = dict(xticks=[0, 1], yticks=[0, 1])  # 刻度，为空刻度即为空
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # frameon图的边框,axprops清空刻度
    plotTree.totalW = float(getNumLeafs(inTree))  # 宽
    plotTree.totalD = float(getTreeDepth(inTree))  # 深度
    plotTree.xOff = -0.5 / plotTree.totalW
    # plotTree.xOff = -1.0 / (plotTree.totalW-1)
    # plotTree.xOff = 0.0
    plotTree.yOff = 1.0
    # plotNode("决策节点", (0.5, 0.1), (0.1, 0.5), decisionNode)
    # plotNode("叶节点", (0.8, 0.1), (0.3, 0.8), leafNode)
    plotTree(inTree, (0.5, 1.0), " ")
    plt.show()

def getNumLeafs(myTree):
    """
    获取叶节点的数目
    :param myTree:
    :return:
    """
    numLeafs = 0
    # firstStr = myTree.keys()[0]
    firstStr = list(myTree.keys())[0]
    secokdDict = myTree[firstStr]
    for key in secokdDict.keys():
        if type(secokdDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secokdDict[key])
        else:
            numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):
    """
    获取数的层数
    :param myTree:
    :return:
    """
    maxDepth = 0
    thisDepth = 0
    # firstStr = myTree.keys()[0] # python2的写法
    firstStr = list(myTree.keys())[0]  # python3需要先转换成list
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth

def plotMidText(cntrPt, parentPt, txtString):
    """
    在父子节点中填充文本信息
    :param cntrPt:
    :param parentPt:
    :param txtString:
    :return:
    """
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeTxt):
    """
    计算节点的位置
    :param myTree:
    :param parentPt:
    :param nodeTxt:
    :return:
    """
    numleafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    '''
    x坐标：如果是叶子节点，则每次递增1/totalW；
    如果是分支节点，则可以算下次有几个节点，这些节点距离上一个节点之间的距离是(1.0 + float(numleafs)) / 2.0 / plotTree.totalW 简单可证
    '''
    cntrPt = (plotTree.xOff + (1.0 + float(numleafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            # plotTree.xOff = plotTree.xOff + 1.0 / (plotTree.totalW-1)
            plotTree.xOff = plotTree.xOff + 1.0 / (plotTree.totalW)
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD

def classify(inputTree, featLabels, testVec):
    """
    使用决策树的分类函数
    :param inputTree:
    :param featLabels:
    :param testVec:
    :return:
    """

    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

def storeTree(inputTree, filename):
    """
    使用pickle模块存储决策树
    :param inputTree:
    :param filename:
    :return:
    """
    import pickle
    # 此处用二进制方式写入
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    """
    使用pickle模块读取决策树
    :param inputTree:
    :param filename:
    :return:
    """
    import pickle
    # 此处用二进制读取
    fr = open(filename, 'rb')
    return pickle.load(fr)

def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                   ]
    return listOfTrees[i]

# print(getNumLeafs(retrieveTree(0)))
# print(getTreeDepth(retrieveTree(0)))
# createPlot(retrieveTree(0))
# myTree, labels = trees.createDataSet()
# print(classify(retrieveTree(0), labels, [1, 0]))
# classify(retrieveTree(0),labels,[1,0])
# storeTree(retrieveTree(0), 'classifierStorage.txt')
# print(grabTree('classifierStorage.txt'))
