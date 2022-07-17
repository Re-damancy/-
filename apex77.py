import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
keywords = input('请输入餐厅关键字：')
param = {
    'cname':'',
    'pid':'',
    'keyword':keywords,
    'pageIndex':'1',
    'pageSize':'10'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
response = requests.post(url=url,data=param,headers=headers)
page_text = response.json()
filename = str(keywords) + '.json'
fp = open(filename,'w',encoding='utf-8')
json.dump(page_text,fp=fp,ensure_ascii=False)
print('成功')