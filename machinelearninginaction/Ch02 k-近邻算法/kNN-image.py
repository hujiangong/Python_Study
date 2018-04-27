from numpy import *
from os import listdir
import machinelearninginaction.Ch02.kNN as kNN

def img2vector(filename):
    """
    将图像转换成测试向量
    :param filename:
    :return:
    """
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):  # 取前32行
        linestr = fr.readline()
        for j in range(32):  # 取每行的前32列
            returnVect[0, 32 * i + j] = int(linestr[j])  # 将每一个值存入返回向量中
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir("imageData/trainingDigits")  # 取训练目录下所有文件名list格式
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])  # 每个文件横线之前的值即为真实值，这里取分类数字
        hwLabels.append(classNumStr)  # 实际数组
        trainingMat[i, :] = img2vector("imageData/trainingDigits/%s" % fileNameStr)  # 将每一个文件内容转换为1024维度的向量
    testFileList = listdir("imageData/testDigits")  # 取测试目录下所有文件名
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split(".")[0]
        classNumStr = int(fileStr.split("_")[0])
        vectorUnderTest = img2vector("imageData/testDigits/%s" % fileNameStr)
        classifierResult = kNN.classify(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print("the total number of errors is: %d" % errorCount)
    print("the total error rate is: %f " % (errorCount / float(mTest)))

handwritingClassTest()
