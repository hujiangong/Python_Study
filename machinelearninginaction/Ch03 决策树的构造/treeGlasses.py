import treePlotter
import trees

'''
使用决策树预测隐形眼镜类型
'''
fr = open('lenses.txt')  # 导入数据
lenses = [inst.strip().split('\t') for inst in fr.readlines()]  # 数据处理
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']  # 打标签
lensesTree = trees.createTree(lenses, lensesLabels)  # 构造树
# print(lensesTree)
treePlotter.createPlot(lensesTree)  # 制图
