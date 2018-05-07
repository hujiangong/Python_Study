# -*- coding: utf-8 -*-

# Define your item pipelines here
# 后续处理
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def process_item(self, item, spider):
        # 这里有问题。爬到的content内容中有/br 时，有分成多个。
        for i in range(0,len(item["content"])):
            print("第"+str(i)+"个："+item["content"][i])
            # print(item["link"][i])
        return item
