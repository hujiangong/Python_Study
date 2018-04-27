# 主成分分析
from sklearn.decomposition import PCA
import pymysql
import pandas as pa
import numpy as py
# 导入数据
data=[[],[]]
# 创建PCA对象
pca1=PCA()
# 加载数据
pca1.fit(data)
# 调出模型的特征量
tz=pca1.components_
# 各个成分中各自方差的百分比，即贡献率(达到85%就可以了)
gxl=pca1.explained_variance_ratio_

# PCA(2)即希望降到几维
pca2=PCA(2)
pca2.fit(data)
# 降维
jw=pca2.transform(data)
# 恢复原本维度
# pca2.inverse_transform(jw)