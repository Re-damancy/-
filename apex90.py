import requests
import os
from lxml import etree
url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=0&classID=864'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
response = requests.get(url=url,headers=headers).text

tree = etree.HTML(response)
l_list = tree.xpath('//div[@class="box col3 ws_block"]')
# print(l_list)
if not os.path.exists('./简历'):
		os.mkdir('./简历')
for li in l_list:
	a_href = 'https:'+li.xpath('./a/@href ')[0]
	a_name = li.xpath('./a/img/@alt')[0]+'.rar'
	#print(a_name)
	#print(a_href)
	down_r = requests.get(url=a_href, headers=headers).text
	#print(down_r)
	d_tree = etree.HTML(down_r)
	d_list = d_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul[1]/li[1]/a/@href')[0]
	d_data = requests.get(url=d_list, headers=headers).content
	d_path = '简历/' + a_name
	with open(d_path, 'wb') as fp:
		fp.write(d_data)
		print(a_name,'完成')
