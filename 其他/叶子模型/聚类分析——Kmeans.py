# -*- coding: utf-8 -*-
# @Time : 2018/3/6 16:25
# @Author : HuJiangong
# @File : 聚类分析——Kmeans.py
# @Version : Python 3.6.4
# @Software: PyCharm

# 导入数据
# cus_all是所有的标签，也可以自定义使用自己需要的标签
cus_general = customer[['wm_poi_id', 'city_type', 'pre_book', 'aor_type', 'is_selfpick_poi', 'is_selfpick_trade_poi']]
cus_ord = customer[['wm_poi_id', 'month_original_price', 'month_order_cnt', 'service_fee_30day', 'abnor_rate_30day']]
cus = customer[['wm_poi_id', 'comment_1star', 'comment_5star', 'pic_comment_cnt']]
cus = customer[['wm_poi_id', 'waybill_received_ratio', 'waybill_delivered_ratio', 'waybill_ontime_ratio',
                'waybill_normal_arrived_delivery_total_interval_avg', 'waybill_normal_poi_push_interval_avg',
                'waybill_normal_receive_interval_avg', 'waybill_normal_fetch_interval_avg',
                'waybill_normal_delivery_interval_avg', 'waybill_delivery_ontime_ratio', 'loss_amt']]
cus_all = customer[['wm_poi_id', 'c5', 'ol_time', 'primary_first_tag_id', 'city_level',
                    'month_original_price', 'month_order_cnt', 'service_fee_30day', 'abnor_cnt_30day',
                    'comment_1star', 'comment_5star', 'pic_comment_cnt',
                    'area_30day', 'waybill_grab_5mins_ratio', 'waybill_delivered_ratio',
                    'waybill_normal_arrived_delivery_total_interval_avg', 'waybill_normal_receive_interval_avg',
                    'call.call_cnt', 'call.call_cnt_ord', 'call.call_cnt_poi', 'call.call_cnt_oth']]

# 预处理
from sklearn import preprocessing

# 归一化（数据必须为数值型数据）
cus = pd.DataFrame(preprocessing.scale(cus_general.iloc[:, 1:6]))
cus = pd.DataFrame(preprocessing.scale(cus_ord.iloc[:, 1:5]))
cus = pd.DataFrame(preprocessing.scale(cus_all.iloc[:, 1:21]))
cus.columns = ['city_type', 'pre_book', 'aor_type', 'is_selfpick_poi', 'is_selfpick_trade_poi']
cus.columns = ['month_original_price', 'month_order_cnt', 'service_fee_30day', 'abnor_rate_30day']
cus.columns = ['comment_1star', 'comment_5star', 'pic_comment_cnt']
cus.columns = ['waybill_push_ratio', 'waybill_delivered_ratio', 'waybill_ontime_ratio',
               'waybill_normal_arrived_delivery_total_interval_avg', 'waybill_normal_poi_push_interval_avg',
               'waybill_normal_receive_interval_avg', 'waybill_normal_fetch_interval_avg',
               'waybill_normal_delivery_interval_avg', 'waybill_delivery_ontime_ratio', 'loss_amt']
cus.columns = ['c5', 'ol_time', 'primary_first_tag_id', 'city_level',
               'month_original_price', 'month_order_cnt', 'service_fee_30day', 'abnor_cnt_30day',
               'comment_1star', 'comment_5star', 'pic_comment_cnt',
               'area_30day', 'waybill_grab_5mins_ratio', 'waybill_delivered_ratio',
               'waybill_normal_arrived_delivery_total_interval_avg', 'waybill_normal_receive_interval_avg',
               'call.call_cnt', 'call.call_cnt_ord', 'call.call_cnt_poi', 'call.call_cnt_oth']

# 计算K值从1到10对应的平均畸变程度：用scipy求解距离
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# K 是指循环一个范围，以确定最后用多少的质心，也就是分多少个类
K = range(1, 15)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters=k)  # 创建k个质心的kmeans模型
    kmeans.fit(cus) # 模型加入数据
    # cdist(cus, kmeans.cluster_centers_, 'euclidean') 计算customer，也就是数据和所有质心之间的距离
    # 之后求出最小的质心距离，然后将所有距离求和，添加到meandistortions
    meandistortions.append(sum(np.min(cdist(cus, kmeans.cluster_centers_, 'euclidean'), axis=1)))
plt.plot(K, meandistortions, 'bx-') # 绘图，选择出拐点，也就是暂定的最合适的质心个数
plt.xlabel('k')
plt.ylabel(u'平均畸变程度')
plt.title(u'用肘部法则来确定最佳的K值')

# Kmean建模
from sklearn.cluster import KMeans

clf = KMeans(n_clusters=12) # 创建12个质心的kmeans模型
clf.fit(cus)
pd.Series(pd.Series(clf.labels_).value_counts()) # 计算属于每个质心的数据个数

centres = pd.DataFrame(clf.cluster_centers_) #
centres.columns = cus_all.iloc[:, 1:21].columns # 取标签
centres.plot(kind='bar', subplots=True, figsize=(6, 15))
clf.inertia_

cus_general = pd.concat([cus_general, pd.DataFrame(clf.fit_predict(cus))], axis=0) # 计算预测值
cus_general = cus_general.rename(columns={0: 'general'})
cus_ord = pd.concat([cus_ord, pd.DataFrame(clf.fit_predict(cus))], axis=0)
cus_ord = cus_ord.rename(columns={0: 'order'})
cus_all = pd.concat([cus_all, pd.DataFrame(clf.fit_predict(cus))], axis=0)
cus_all = cus_all.rename(columns={0: 'cluster'})

centres = cus_all.groupby(['cluster']).mean()

cus_all.to_csv('cluster.csv') # 导出

result = cus_all[cus_all['cluster'] == 2]
