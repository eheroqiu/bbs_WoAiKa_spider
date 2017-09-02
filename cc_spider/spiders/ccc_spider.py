# -*- coding: utf-8 -*-
import re 
import json
import codecs
import scrapy
import copy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log
from cc_spider.items import CcSpiderItem


class CccSpiderSpider(scrapy.Spider):
    name = "ccc_spider"
    #allowed_domains = ["bbs.51credit.com"]
    #start_urls = ['http://bbs.51credit.com/forum-8-1.html']
    def start_requests(self):
        for i in range(1,500):
            #url='http://bbs.51credit.com/forum.php?mod=forumdisplay&fid=8&page='+str(i)
            #url='http://bbs.51credit.com/forum.php?mod=forumdisplay&fid=13&filter=typeid&typeid=252&page='+str(i)
            url='http://bbs.51credit.com/forum-13-'+str(i)+'.html'
    	    yield Request(url
                ,cookies={'_d': '', 'USERID': '1042660662', 'ROOTTGT': 'TGT-3558-AWb1torNozD7doUACfxJ3X4fnGXRg9GYiToaOy3IxzgTS4v1zj-cas', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2215b0dec23561bc-0cc0d329f537d6-1262694a-2073600-15b0dec2357407%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D', 'kcjY_2132_security_cookiereport': '8e4dsLAG0DNfaQUolErOoCMAgKne%2FIS98%2BKZTyxX3qxHGwGrLe79', 'kcjY_2132_saltkey': 'S1nSu6aA', 'Hm_lvt_d256e4b92cfb8c5174fae259762d07ce': '1490684584', 'Hm_lvt_3dedf380c2bfdaac814bc570f6ac0740': '1490587261,1490589447,1490589754,1490836524', 'CNZZDATA4008412': 'cnzz_eid%3D534924422-1490586527-http%253A%252F%252Fbbs.51credit.com%252F%26ntime%3D1490840352', 'indexadHide': '1', 'kcjY_2132_atarget': '1', 'kcjY_2132_ulastactivity': 'a00b1mxBYiS44%2BbNTj1hM725vTYrGNMlKEm4vo4kxOwr8CG9wREr', 'kcjY_2132_noticeTitle': '1', '_t': 'ijTrGSAqzNLN25Yrijnoi9boLCCaMXzI%2Fko6DbprO1Nu2SBoY83A4QmEwwFU31jfFosmPjGik5qS%0D%0AEsQHGBqKjQ%3D%3D%0D%0A', 'kcjY_2132_nofavfid': '1', 'kcjY_2132_pc_size_c': '0', 'pgv_info': 'ssi', 'kcjY_2132_sid': 'pY06AM', 'DESCU3': '1e2286855db5891476a75a91f370950e', 'kcjY_2132_smile': '1D1', 'Hm_lpvt_2368db03d58b3a9c27ac58870c989566': '1490842283', 'pgv_pvi': '8680611694', 'CNZZDATA1257371675': '372922344-1490586073-http%253A%252F%252Fbbs.51credit.com%252F%7C1490839891', 'USERNAME': 'kashen16067908', 'kcjY_2132_lastact': '1490842257%09home.php%09misc', 'Hm_lpvt_3dedf380c2bfdaac814bc570f6ac0740': '1490842284', 'CNZZDATA1254451435': '2069051341-1490587000-http%253A%252F%252Fbbs.51credit.com%252F%7C1490840836', 'hideLayer': '1', 'Hm_lpvt_ed2cce1d377593c5a0c03e66ded87152': '1490842284', 'kcjY_2132_viewid': 'tid_2271971', 'UM_distinctid': '15b0dec34e132c-0ea6d21d2b56fe-1262694a-1fa400-15b0dec34e225c', 'kcjY_2132_lastvisit': '1490583506', 'Hm_lvt_2368db03d58b3a9c27ac58870c989566': '1490587261,1490589447,1490589754,1490836524', 'Hm_lvt_ed2cce1d377593c5a0c03e66ded87152': '1490587261,1490589447,1490589754,1490836524', 'SERVICEURL': '', 'USERAUTHCODE': 'bf5f9b378b548bf296a2b235b87b00ed', 'kcjY_2132_forum_lastvisit': 'D_235_1490589437D_8_1490842255', 'PISCHANGED': '1'}
    		    , callback=self.parse_with_cookie)
    def parse_detail(self, response):
        next_url=response.xpath("//div[@class='pgbtn']/a[@class='bm_h']/@href").extract()
        s=response.xpath("//div[@class='pct']/div[@class='pcb']/div[@class='t_fsz']/table[@cellspacing='0']/tr/td[@class='t_f']/text()").extract()
        y=(filter (lambda x: x not in (u'\n',u'\r\n',u'\r'),s))
        #cnt=len(y)
        if len(next_url)==0:
            for i in y:
            #for i in range(0,cnt-1):
                item=CcSpiderItem()
                item['title']=response.meta['title']
                item['pl_text']=i.strip('\n').strip('\r\n')
                yield item
        else:
            for i in y:
                item=CcSpiderItem()
                item['title']=response.meta['title']
                item['pl_text']=i.strip('\n').strip('\r\n')
                yield item
            yield Request('http://bbs.51credit.com/'+next_url[0], 
                cookies={'_d': '', 'USERID': '1042660662', 'ROOTTGT': 'TGT-3558-AWb1torNozD7doUACfxJ3X4fnGXRg9GYiToaOy3IxzgTS4v1zj-cas'
                , 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2215b0dec23561bc-0cc0d329f537d6-1262694a-2073600-15b0dec2357407%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
                , 'kcjY_2132_security_cookiereport': '8e4dsLAG0DNfaQUolErOoCMAgKne%2FIS98%2BKZTyxX3qxHGwGrLe79', 'kcjY_2132_saltkey': 'S1nSu6aA', 'Hm_lvt_d256e4b92cfb8c5174fae259762d07ce': '1490684584'
                , 'Hm_lvt_3dedf380c2bfdaac814bc570f6ac0740': '1490587261,1490589447,1490589754,1490836524', 'CNZZDATA4008412': 'cnzz_eid%3D534924422-1490586527-http%253A%252F%252Fbbs.51credit.com%252F%26ntime%3D1490840352', 'indexadHide': '1', 'kcjY_2132_atarget': '1', 'kcjY_2132_ulastactivity': 'a00b1mxBYiS44%2BbNTj1hM725vTYrGNMlKEm4vo4kxOwr8CG9wREr'
                , 'kcjY_2132_noticeTitle': '1', '_t': 'ijTrGSAqzNLN25Yrijnoi9boLCCaMXzI%2Fko6DbprO1Nu2SBoY83A4QmEwwFU31jfFosmPjGik5qS%0D%0AEsQHGBqKjQ%3D%3D%0D%0A', 'kcjY_2132_nofavfid': '1', 'kcjY_2132_pc_size_c': '0', 'pgv_info': 'ssi', 'kcjY_2132_sid': 'pY06AM', 'DESCU3': '1e2286855db5891476a75a91f370950e', 'kcjY_2132_smile': '1D1', 'Hm_lpvt_2368db03d58b3a9c27ac58870c989566': '1490842283'
                , 'pgv_pvi': '8680611694', 'CNZZDATA1257371675': '372922344-1490586073-http%253A%252F%252Fbbs.51credit.com%252F%7C1490839891', 'USERNAME': 'kashen16067908', 'kcjY_2132_lastact': '1490842257%09home.php%09misc', 'Hm_lpvt_3dedf380c2bfdaac814bc570f6ac0740': '1490842284', 'CNZZDATA1254451435': '2069051341-1490587000-http%253A%252F%252Fbbs.51credit.com%252F%7C1490840836', 'hideLayer': '1', 'Hm_lpvt_ed2cce1d377593c5a0c03e66ded87152': '1490842284', 'kcjY_2132_viewid': 'tid_2271971', 'UM_distinctid': '15b0dec34e132c-0ea6d21d2b56fe-1262694a-1fa400-15b0dec34e225c', 'kcjY_2132_lastvisit': '1490583506', 'Hm_lvt_2368db03d58b3a9c27ac58870c989566': '1490587261,1490589447,1490589754,1490836524', 'Hm_lvt_ed2cce1d377593c5a0c03e66ded87152': '1490587261,1490589447,1490589754,1490836524', 'SERVICEURL': '', 'USERAUTHCODE': 'bf5f9b378b548bf296a2b235b87b00ed', 'kcjY_2132_forum_lastvisit': 'D_235_1490589437D_8_1490842255', 'PISCHANGED': '1'}
                ,callback=self.parse_detail, meta={'title':title})
        #item =response.meta['item']
        #f=open('link','a')
        #curr_page_url=response.xpath("//a[@rel='nofollow']/@href")[0].extract()
        #curr_page=curr_page_url.split('=')[3]
        #page_code=curr_page[0:curr_page.index('&')]
        #next_url=response.xpath("//div[@class='pgbtn']/a[@class='bm_h']/@href").extract()
        #s=response.xpath("//div[@class='pct']/div[@class='pcb']/div[@class='t_fsz']/table[@cellspacing='0']/tr/td[@class='t_f']/text()").extract()
        #item['pl_text']=(filter (lambda x: x not in (u'\n',u'\r\n'),s))
        #if len(next_url)==0:
        #    yield item
        #else:
        #    yield Request('http://bbs.51credit.com/'+next_url[0], 
        #        cookies={'_d': '', 'USERID': '1042660662', 'ROOTTGT': 'TGT-3558-AWb1torNozD7doUACfxJ3X4fnGXRg9GYiToaOy3IxzgTS4v1zj-cas'
        #        , 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2215b0dec23561bc-0cc0d329f537d6-1262694a-2073600-15b0dec2357407%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
        #        , 'kcjY_2132_security_cookiereport': '8e4dsLAG0DNfaQUolErOoCMAgKne%2FIS98%2BKZTyxX3qxHGwGrLe79', 'kcjY_2132_saltkey': 'S1nSu6aA', 'Hm_lvt_d256e4b92cfb8c5174fae259762d07ce': '1490684584'
        #        , 'Hm_lvt_3dedf380c2bfdaac814bc570f6ac0740': '1490587261,1490589447,1490589754,1490836524', 'CNZZDATA4008412': 'cnzz_eid%3D534924422-1490586527-http%253A%252F%252Fbbs.51credit.com%252F%26ntime%3D1490840352', 'indexadHide': '1', 'kcjY_2132_atarget': '1', 'kcjY_2132_ulastactivity': 'a00b1mxBYiS44%2BbNTj1hM725vTYrGNMlKEm4vo4kxOwr8CG9wREr'
        #        , 'kcjY_2132_noticeTitle': '1', '_t': 'ijTrGSAqzNLN25Yrijnoi9boLCCaMXzI%2Fko6DbprO1Nu2SBoY83A4QmEwwFU31jfFosmPjGik5qS%0D%0AEsQHGBqKjQ%3D%3D%0D%0A', 'kcjY_2132_nofavfid': '1', 'kcjY_2132_pc_size_c': '0', 'pgv_info': 'ssi', 'kcjY_2132_sid': 'pY06AM', 'DESCU3': '1e2286855db5891476a75a91f370950e', 'kcjY_2132_smile': '1D1', 'Hm_lpvt_2368db03d58b3a9c27ac58870c989566': '1490842283'
        #        , 'pgv_pvi': '8680611694', 'CNZZDATA1257371675': '372922344-1490586073-http%253A%252F%252Fbbs.51credit.com%252F%7C1490839891', 'USERNAME': 'kashen16067908', 'kcjY_2132_lastact': '1490842257%09home.php%09misc', 'Hm_lpvt_3dedf380c2bfdaac814bc570f6ac0740': '1490842284', 'CNZZDATA1254451435': '2069051341-1490587000-http%253A%252F%252Fbbs.51credit.com%252F%7C1490840836', 'hideLayer': '1', 'Hm_lpvt_ed2cce1d377593c5a0c03e66ded87152': '1490842284', 'kcjY_2132_viewid': 'tid_2271971', 'UM_distinctid': '15b0dec34e132c-0ea6d21d2b56fe-1262694a-1fa400-15b0dec34e225c', 'kcjY_2132_lastvisit': '1490583506', 'Hm_lvt_2368db03d58b3a9c27ac58870c989566': '1490587261,1490589447,1490589754,1490836524', 'Hm_lvt_ed2cce1d377593c5a0c03e66ded87152': '1490587261,1490589447,1490589754,1490836524', 'SERVICEURL': '', 'USERAUTHCODE': 'bf5f9b378b548bf296a2b235b87b00ed', 'kcjY_2132_forum_lastvisit': 'D_235_1490589437D_8_1490842255', 'PISCHANGED': '1'}
        #        ,callback=self.parse_detail, meta={'title':title})
        #f=open('body_detail','w')
        #f.write(response.body.decode('gbk').encode('utf8'))
        #f.close()
        #print page_code
        #s=response.xpath("//div[@class='pct']/div[@class='pcb']/div[@class='t_fsz']/table[@cellspacing='0']/tr/td[@class='t_f']/text()").extract()
        #if page_code=='1':
        #    item['pl_text']=(filter (lambda x: x not in (u'\n',u'\r\n'),s))
        #    if len(next_url)==0:
        #        yield item
        #    else:
        #        yield Request('http://bbs.51credit.com/'+next_url[0], 
        #            cookies={'_d': '', 'USERID': '1042660662', 'ROOTTGT': 'TGT-3558-AWb1torNozD7doUACfxJ3X4fnGXRg9GYiToaOy3IxzgTS4v1zj-cas'
        #            , 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2215b0dec23561bc-0cc0d329f537d6-1262694a-2073600-15b0dec2357407%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
        #            , 'kcjY_2132_security_cookiereport': '8e4dsLAG0DNfaQUolErOoCMAgKne%2FIS98%2BKZTyxX3qxHGwGrLe79', 'kcjY_2132_saltkey': 'S1nSu6aA', 'Hm_lvt_d256e4b92cfb8c5174fae259762d07ce': '1490684584'
        #            , 'Hm_lvt_3dedf380c2bfdaac814bc570f6ac0740': '1490587261,1490589447,1490589754,1490836524', 'CNZZDATA4008412': 'cnzz_eid%3D534924422-1490586527-http%253A%252F%252Fbbs.51credit.com%252F%26ntime%3D1490840352', 'indexadHide': '1', 'kcjY_2132_atarget': '1', 'kcjY_2132_ulastactivity': 'a00b1mxBYiS44%2BbNTj1hM725vTYrGNMlKEm4vo4kxOwr8CG9wREr'
        #            , 'kcjY_2132_noticeTitle': '1', '_t': 'ijTrGSAqzNLN25Yrijnoi9boLCCaMXzI%2Fko6DbprO1Nu2SBoY83A4QmEwwFU31jfFosmPjGik5qS%0D%0AEsQHGBqKjQ%3D%3D%0D%0A', 'kcjY_2132_nofavfid': '1', 'kcjY_2132_pc_size_c': '0', 'pgv_info': 'ssi', 'kcjY_2132_sid': 'pY06AM', 'DESCU3': '1e2286855db5891476a75a91f370950e', 'kcjY_2132_smile': '1D1', 'Hm_lpvt_2368db03d58b3a9c27ac58870c989566': '1490842283'
        #            , 'pgv_pvi': '8680611694', 'CNZZDATA1257371675': '372922344-1490586073-http%253A%252F%252Fbbs.51credit.com%252F%7C1490839891', 'USERNAME': 'kashen16067908', 'kcjY_2132_lastact': '1490842257%09home.php%09misc', 'Hm_lpvt_3dedf380c2bfdaac814bc570f6ac0740': '1490842284', 'CNZZDATA1254451435': '2069051341-1490587000-http%253A%252F%252Fbbs.51credit.com%252F%7C1490840836', 'hideLayer': '1', 'Hm_lpvt_ed2cce1d377593c5a0c03e66ded87152': '1490842284', 'kcjY_2132_viewid': 'tid_2271971', 'UM_distinctid': '15b0dec34e132c-0ea6d21d2b56fe-1262694a-1fa400-15b0dec34e225c', 'kcjY_2132_lastvisit': '1490583506', 'Hm_lvt_2368db03d58b3a9c27ac58870c989566': '1490587261,1490589447,1490589754,1490836524', 'Hm_lvt_ed2cce1d377593c5a0c03e66ded87152': '1490587261,1490589447,1490589754,1490836524', 'SERVICEURL': '', 'USERAUTHCODE': 'bf5f9b378b548bf296a2b235b87b00ed', 'kcjY_2132_forum_lastvisit': 'D_235_1490589437D_8_1490842255', 'PISCHANGED': '1'}
        #            ,callback=self.parse_detail, meta={'item':item})
        #else:
        #    item['pl_text'].extend(filter (lambda x: x not in (u'\n',u'\r\n'),s))
        #    if len(next_url)==0:
        #        yield item
        #    else:
        #        yield Request('http://bbs.51credit.com/'+next_url[0], 
        #            cookies={'_d': '', 'USERID': '1042660662', 'ROOTTGT': 'TGT-3558-AWb1torNozD7doUACfxJ3X4fnGXRg9GYiToaOy3IxzgTS4v1zj-cas'
        #            , 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2215b0dec23561bc-0cc0d329f537d6-1262694a-2073600-15b0dec2357407%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
        #            , 'kcjY_2132_security_cookiereport': '8e4dsLAG0DNfaQUolErOoCMAgKne%2FIS98%2BKZTyxX3qxHGwGrLe79', 'kcjY_2132_saltkey': 'S1nSu6aA', 'Hm_lvt_d256e4b92cfb8c5174fae259762d07ce': '1490684584'
        #            , 'Hm_lvt_3dedf380c2bfdaac814bc570f6ac0740': '1490587261,1490589447,1490589754,1490836524', 'CNZZDATA4008412': 'cnzz_eid%3D534924422-1490586527-http%253A%252F%252Fbbs.51credit.com%252F%26ntime%3D1490840352', 'indexadHide': '1', 'kcjY_2132_atarget': '1', 'kcjY_2132_ulastactivity': 'a00b1mxBYiS44%2BbNTj1hM725vTYrGNMlKEm4vo4kxOwr8CG9wREr'
        #            , 'kcjY_2132_noticeTitle': '1', '_t': 'ijTrGSAqzNLN25Yrijnoi9boLCCaMXzI%2Fko6DbprO1Nu2SBoY83A4QmEwwFU31jfFosmPjGik5qS%0D%0AEsQHGBqKjQ%3D%3D%0D%0A', 'kcjY_2132_nofavfid': '1', 'kcjY_2132_pc_size_c': '0', 'pgv_info': 'ssi', 'kcjY_2132_sid': 'pY06AM', 'DESCU3': '1e2286855db5891476a75a91f370950e', 'kcjY_2132_smile': '1D1', 'Hm_lpvt_2368db03d58b3a9c27ac58870c989566': '1490842283'
        #            , 'pgv_pvi': '8680611694', 'CNZZDATA1257371675': '372922344-1490586073-http%253A%252F%252Fbbs.51credit.com%252F%7C1490839891', 'USERNAME': 'kashen16067908', 'kcjY_2132_lastact': '1490842257%09home.php%09misc', 'Hm_lpvt_3dedf380c2bfdaac814bc570f6ac0740': '1490842284', 'CNZZDATA1254451435': '2069051341-1490587000-http%253A%252F%252Fbbs.51credit.com%252F%7C1490840836', 'hideLayer': '1', 'Hm_lpvt_ed2cce1d377593c5a0c03e66ded87152': '1490842284', 'kcjY_2132_viewid': 'tid_2271971', 'UM_distinctid': '15b0dec34e132c-0ea6d21d2b56fe-1262694a-1fa400-15b0dec34e225c', 'kcjY_2132_lastvisit': '1490583506', 'Hm_lvt_2368db03d58b3a9c27ac58870c989566': '1490587261,1490589447,1490589754,1490836524', 'Hm_lvt_ed2cce1d377593c5a0c03e66ded87152': '1490587261,1490589447,1490589754,1490836524', 'SERVICEURL': '', 'USERAUTHCODE': 'bf5f9b378b548bf296a2b235b87b00ed', 'kcjY_2132_forum_lastvisit': 'D_235_1490589437D_8_1490842255', 'PISCHANGED': '1'}
        #            ,callback=self.parse_detail, meta={'item':item})
    def parse_with_cookie(self, response):
        #f=open('body_detail','a')
        #f.write(response.body.decode('gbk').encode('utf8'))
        #f.close()
        #@class='lock'
    	cnt=len(response.xpath("//th[@class]/a[@onclick]/@href").extract())
        print str(cnt)+'####################################################'
        for i in range(0,cnt-1):
    	#for i in range(0,cnt-1):
            #item['link']='http://bbs.51credit.com/'+response.xpath("//th[@class='new']/a[@class]/@href")[i].extract()
            global title
            title=response.xpath("//th[@class]/a[@onclick]/text()")[i].extract() 
            url='http://bbs.51credit.com/'+response.xpath("//th[@class]/a[@onclick]/@href")[i].extract()
            yield Request(url, 
                cookies={'_d': '', 'USERID': '1042660662', 'ROOTTGT': 'TGT-3558-AWb1torNozD7doUACfxJ3X4fnGXRg9GYiToaOy3IxzgTS4v1zj-cas'
                , 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2215b0dec23561bc-0cc0d329f537d6-1262694a-2073600-15b0dec2357407%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
                , 'kcjY_2132_security_cookiereport': '8e4dsLAG0DNfaQUolErOoCMAgKne%2FIS98%2BKZTyxX3qxHGwGrLe79', 'kcjY_2132_saltkey': 'S1nSu6aA', 'Hm_lvt_d256e4b92cfb8c5174fae259762d07ce': '1490684584'
                , 'Hm_lvt_3dedf380c2bfdaac814bc570f6ac0740': '1490587261,1490589447,1490589754,1490836524', 'CNZZDATA4008412': 'cnzz_eid%3D534924422-1490586527-http%253A%252F%252Fbbs.51credit.com%252F%26ntime%3D1490840352', 'indexadHide': '1', 'kcjY_2132_atarget': '1', 'kcjY_2132_ulastactivity': 'a00b1mxBYiS44%2BbNTj1hM725vTYrGNMlKEm4vo4kxOwr8CG9wREr'
                , 'kcjY_2132_noticeTitle': '1', '_t': 'ijTrGSAqzNLN25Yrijnoi9boLCCaMXzI%2Fko6DbprO1Nu2SBoY83A4QmEwwFU31jfFosmPjGik5qS%0D%0AEsQHGBqKjQ%3D%3D%0D%0A', 'kcjY_2132_nofavfid': '1', 'kcjY_2132_pc_size_c': '0', 'pgv_info': 'ssi', 'kcjY_2132_sid': 'pY06AM', 'DESCU3': '1e2286855db5891476a75a91f370950e', 'kcjY_2132_smile': '1D1', 'Hm_lpvt_2368db03d58b3a9c27ac58870c989566': '1490842283'
                , 'pgv_pvi': '8680611694', 'CNZZDATA1257371675': '372922344-1490586073-http%253A%252F%252Fbbs.51credit.com%252F%7C1490839891', 'USERNAME': 'kashen16067908', 'kcjY_2132_lastact': '1490842257%09home.php%09misc', 'Hm_lpvt_3dedf380c2bfdaac814bc570f6ac0740': '1490842284', 'CNZZDATA1254451435': '2069051341-1490587000-http%253A%252F%252Fbbs.51credit.com%252F%7C1490840836', 'hideLayer': '1', 'Hm_lpvt_ed2cce1d377593c5a0c03e66ded87152': '1490842284', 'kcjY_2132_viewid': 'tid_2271971', 'UM_distinctid': '15b0dec34e132c-0ea6d21d2b56fe-1262694a-1fa400-15b0dec34e225c', 'kcjY_2132_lastvisit': '1490583506', 'Hm_lvt_2368db03d58b3a9c27ac58870c989566': '1490587261,1490589447,1490589754,1490836524', 'Hm_lvt_ed2cce1d377593c5a0c03e66ded87152': '1490587261,1490589447,1490589754,1490836524', 'SERVICEURL': '', 'USERAUTHCODE': 'bf5f9b378b548bf296a2b235b87b00ed', 'kcjY_2132_forum_lastvisit': 'D_235_1490589437D_8_1490842255', 'PISCHANGED': '1'}
                ,callback=self.parse_detail, meta={'title':title})




    	#f=open('body_detail','a')
    	#f.write(response.body.decode('gbk').encode('utf8'))
    	#f.close()
        
