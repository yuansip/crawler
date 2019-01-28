# -*- coding: utf-8 -*-

import scrapy
import json
import urlparse

from sjjyspider.items import SjjyspiderItem


def url_replacer(url, key, value):
    c_url_list = list(urlparse.urlparse(url))
    queries = [q.split('=') for q in c_url_list[4].split('&')]
    for v in queries:
        if v[0] == key:
            v[1] = value
            break

    c_url_list[4] = '&'.join(map(lambda l: '='.join(l), queries))
    return urlparse.urlunparse(c_url_list)

class SjjySpider(scrapy.Spider):
    name = "sjjy"
    allowed_domains = ["jiayuan.com"]
    start_urls = [
        "http://search.jiayuan.com/v2/search_v2.php?key=&sex=f&stc=1:11,2:18.24,3:155.170,23:1&sn=default&sv=1&p=1&f=select"
    ]

    def parse(self, response):
        # datas = json.dumps(response.text, ensure_ascii= False, indent=4, separators=(',', ': '))
        # jsonstr = json.loads(datas).encode('utf-8').decode('unicode_escape')
        # jresp = json.loads(jsonstr)
        jresp = json.loads(response.body_as_unicode())
        pageTotal = jresp['pageTotal']
        for user in jresp["userInfo"]:
            # print user['shortnote']
            item = SjjyspiderItem()
            item['nickname'] = user['nickname']
            item['gender'] = user['sexValue']
            item['marriage'] = user['marriage']
            item['height'] = user['height']
            item['education'] = user['education']
            item['age'] = user['age']
            item['short_note'] = user['shortnote']
            item['image_urls'] = [user['image']]
            yield item

        if pageTotal > 1:
            for i in range(2, pageTotal+1):
                u = url_replacer(self.start_urls[0], 'p', str(i))
                yield scrapy.Request(u)
