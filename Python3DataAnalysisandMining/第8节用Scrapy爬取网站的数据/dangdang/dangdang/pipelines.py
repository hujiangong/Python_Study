# -*- coding: utf-8 -*-

import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        # 这里需要设置charset="utf8"，否则会报“UnicodeEncodeError: 'latin-1' codec can't encode characters in position 61-63: ordinal not in range(256)” 错误。
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="dangdang", charset="utf8")
        # print(item["title"])
        # print(item["link"])
        # print(item["comment"])
        for i in range(len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            sql = "insert into detail (title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            conn.query(sql)
            conn.commit()
        conn.close()
        return item
