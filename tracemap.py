#!/usr/bin/python2.7
import requests
import ast
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file=open("/root/github/traceme/ip.txt","r")

ip=[]
for i in file.readlines():
	ip.append(i.strip())
#print ip

city=[]
latitude=[]
longitude=[]
for i in range(len(ip)):
	response=requests.get("http://ip-api.com/json/"+ip[i])
	if "fail" not in response.content:
		response_dict=ast.literal_eval(response.content)
		city.append(response_dict['city'])
		latitude.append(response_dict['lat'])
		longitude.append(response_dict['lon'])
		#print response.content

print city,"\n",latitude,"\n",longitude

map = Basemap(projection='cyl')
plt.title("WorldMap")
map.drawcoastlines()
map.drawmapboundary(fill_color="#7777ff")
map.fillcontinents(color="#ddaa66",lake_color="#7777ff")

for i in range(len(city)):
	x,y = map(longitude[i],latitude[i])
	map.plot(x,y,'g^',markersize=10)
	plt.text(x,y,city[i],fontsize=6,fontweight='bold',ha='left',va='bottom',color='#8B008B', bbox=dict(facecolor='b', alpha=.1))

x,y = map(longitude,latitude)

map.plot(x,y,color='r',linewidth=2,label="DataFlow")
plt.legend(loc=4)
x,y=map(-170,-82)
plt.text(x,y,city,fontsize=6,fontweight='bold')

plt.savefig('map.png',dpi=1000,bbox_inches='tight')
plt.show()
