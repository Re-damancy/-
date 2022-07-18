import requests
import re
import os
#创建一个文件夹，保存所有图片
if not os.path.exists('./touxiang'):
	os.mkdir('./touxiang')
	#设置一个通用的url模板
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
url = 'https://www.woyaogexing.com/touxiang/z/nandongman/index_%d.html'
#https://www.woyaogexing.com/touxiang/z/nandongman/index_2.html
#pageNum = 2
for pageNum in range(2,4):
	#对应页码的url
	new_url = (f"{url%pageNum}")


	page_text = requests.get(url=new_url,headers=headers).text

	#使用聚焦爬虫对页面中的图片进行爬取，正则表达式！！！！！！
	ex = '<div class="txList ">.*?<img class="lazy" src="(.*?)" width.*?</div>'
	img_src_list = re.findall(ex,page_text,re.S)

	for src in img_src_list:
		#拼接处一个完整的图片url
		src = 'https:'+src
		#请求到了图片的二进制数据
		img_data = requests.get(url=src,headers=headers).content
		#生成图片名称
		img_name = src.split('/')[-1]
		#图片储存的路径
		imgPath = './touxiang/'+img_name
		with open(imgPath,'wb') as fp:
			fp.write(img_data)
			print(img_name,'下载成功!!!')
