# -*- coding: UTF-8 -*-
#设置字符编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

def getCommentCounts(newsurl):
	m = re.search('doc-i(.*).shtml',newsurl)
	newsid = m.group(1)
	commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&page=1&page_size=20'
	comments = requests.get(commentURL.format(newsid))
	#print(commentURL.format(newsid))
	jd = json.loads(comments.text.strip('var data='))
	return jd['result']['count']['total']

def getNewsDetail(newsurl):
	result = {}
	res = requests.get(newsurl)
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,'html.parser')
	result['title'] = soup.select('#artibodyTitle')[0].text
	result['newssource'] = soup.select('.time-source span a')[0].text
	timesouce = soup.select('.time-source')[0].contents[0].strip()
	result['dt'] = datetime.strptime(timesouce,'%Y年%m月%d日%H:%M')
	result['article'] = ''.join([p.text.strip()for p in soup.select('#artibody p')[:-1]])
	result['comments'] = getCommentCounts(newsurl)
	#return result
	print result['title'],"\n",result['article'],"\n新闻来源：",result['newssource'],"\n发布时间：",result['dt'],"\n评论数：",result['comments']

if __name__ == '__main__':
    getNewsDetail(raw_input('请输入爬取的urls:'))
