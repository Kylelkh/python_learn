#-*- coding:utf-8 -*-
#爬取赶集网住房信息并导入csv表中
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

URL = "http://bj.ganji.com/fang1/o{page}p{price}/"
ADDR = "http://bj.ganji.com/"

if __name__ == '__main__':
	print "chushihua"
	start_page = 1
	end_page = 2
	price =7 
	with open("house_info.csv","wb") as f:
		csv_writer = csv.writer(f,delimiter=",")
		print "start.."
		while start_page < end_page:
			start_page +=1
			print "get:{0}".format(URL.format(page=start_page,price=price))
			response = requests.get(URL.format(page=start_page,price=price))
			html = BeautifulSoup(response.text,"html.parser")
			html_list = html.select(".f-list > .f-list-item > .f-list-item-wrap")
			if not html_list:
				print "error."
				break
			for house in html_list:
				house_title = house.select(".title > a")[0].string.encode("utf8")
				house_addr = house.select(".address > .area > a")[-1].string.encode("utf8")
				house_price = house.select(".info > .price > .num")[0].string.encode("utf8")
				house_url = urljoin(ADDR,house.select(".title > a")[0]["href"])
				csv_writer.writerow([house_title,house_addr,house_price,house_url])
			print "end"

