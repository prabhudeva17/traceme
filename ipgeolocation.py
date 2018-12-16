#!/usr/bin/python2.7
import requests
import ast
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

file=open("/root/github/traceme/ip.txt","r")

ip=[]
for i in file.readlines():
	#print i.strip()
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

map=Basemap(projection='mill')
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

x,y = map(longitude,latitude)
#x,y = map(logitude,latitude)
map.plot(x,y,marker='^',color='m')

plt.show()