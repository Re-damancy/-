import plotly.express as px
import pandas as pd#导入pandas
import json#导入json

filename = 'eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)#导入模块JSON并将其储存在其中 json.load()将数据转化成Python能够处理的格式
	all_eq_dicts = all_eq_data['features']#在存储的数据中提取与键相关的数据存储到另一个中
	print(len(all_eq_dicts))#打印地震次数

mags,titles,lons,lats,lyts = [],[],[],[],[]
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	title = eq_dict['properties']['title']
	lon = eq_dict['geometry']['coordinates'][0]#索引0提取该列表中的第一个值
	lat = eq_dict['geometry']['coordinates'][1]#索引1提取该列表中的第二个值
	lyt = eq_dict['geometry']['coordinates'][2]
	mags.append(mag)
	titles.append(title)
	lons.append(lon)
	lats.append(lat)
	lyts.append(lyt)
#print(mags[:10])#使用切片打印前10次地震的震级
data = pd.DataFrame(
	data=zip(lons,lats,titles,mags),columns=['经度','维度','位置','震级']
	)
data.head()#24-27将图中的X和Y替换的另一种方式
#print(titles[:2])
#print(lons[:5])
#print(lats[:5])
#print(lyts[:5])
fig = px.scatter(
		data,#参数配置
		x=lons,
		y=lats,
		labels={'x':'经度','y':'纬度'},#将图中的X和Y替换
		range_x=[-200,200],
		range_y=[-90,90],
		width=800,
		height=800,
		title='全球地震散点图',
		size='震级',
		size_max=10,
		color='震级',
		color_continuous_scale='phase',#设置渐变色
		hover_name='位置',#添加了鼠标指向的一个参数配置为data的'位置'
		)
fig.write_html('global_earthquakes.html')
fig.show()