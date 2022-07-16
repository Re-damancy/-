import requests
import urllib3#记得加
from plotly.graph_objs import Bar
from plotly import offline


urllib3.disable_warnings()#和第二行一样

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'#储存API调用的URL
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers,verify=False)#再使用requests调用API
print(f"Status code:{r.status_code}")
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names,stars = [],[]
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

data = [{
	'type':'bar',
	'x':repo_names,
	'y':stars,
	'marker':{
		'color':'rgb(60,100,150)',
		'line':{'width':1.5,'color':'rgb(25,25,25)'}
	},
	'opacity':0.6
}]
my_layout = {
	'title':'Github上最受欢迎的Python项目',
	'titlefont':{'size':28},
	'titlefont':{'size':14},
	'xaxis':{'title':'仓库'},
	'yaxis':{'title':'星级'}
}

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos,html')
