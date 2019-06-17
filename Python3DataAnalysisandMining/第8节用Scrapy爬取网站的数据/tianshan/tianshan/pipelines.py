# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting ！！！！
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TianshanPipeline(object):
    def __init__(self):
        # 这里指定写入文件的格式
        self.file = open("result.txt", "w", encoding='utf-8')

    def process_item(self, item, spider):
        # print(item['title'])
        # print(item['link'])
        # print(item['stu'])
        # print(item['price'])
        # print(len(item['price']))
        # print('--------------------')
        self.file.write("课程名：" + str(item['title'][0]))
        self.file.write("\n")
        self.file.write("课程链接：" + str(item['link'][0]))
        self.file.write("\n")
        self.file.write("学习人数：" + str(item['stu'][0]))
        self.file.write("\n")
        # self.file.write("课程价格：" + str(item['price']))
        # self.file.write("\n")
        self.file.write("-------------------------------------")
        self.file.write("\n")
        return item

    def close_spider(self, spider):
        """
        这里注意，需要传进来两个参数，视频课程中一个参数是错误的
        :param spider:
        :return:
        """
        self.file.close()
