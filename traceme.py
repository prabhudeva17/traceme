#!/usr/bin/python2.7
import scapy.all as scapy
import argparse
import requests
import ast
import simplekml

print "\nTraceRoute Started *****"

parser=argparse.ArgumentParser()
parser.add_argument("-i","--host",dest="host",help="Give Hostname or IP Address")
parser.parse_args()
options=parser.parse_args()

print "Host:",options.host

def traceroute():
	ip_addr=[]
	for i in range(1,50):
		icmp=scapy.IP(dst=options.host,ttl=i)/scapy.ICMP()
		b=scapy.sr1(icmp,timeout=3,verbose=False)
		try:

			if i==1:
				src_ip=b.dst
				print "\nSource_IP:%s\n"%src_ip
		
		except AttributeError:
			pass
					
		if b is None:
			print "TTL=%s \t*****Router Drops the packet*****"%i

		else:
			if b.src in ip_addr:
				dst_ip=b.src
				print "\nDestination_IP:%s\n"%dst_ip
				break

			print "TTL=%s \tIntermediate_IP=%s"%(i,b.src)
			ip_addr.append(b.src)
	return ip_addr

def getlocation():
	city=[]
	latitude=[]
	longitude=[]
	for i in range(len(ipaddr)):
		response=requests.get("http://ip-api.com/json/"+ipaddr[i])
		if "fail" not in response.content:
			response_dict=ast.literal_eval(response.content)
			city.append(response_dict['city'])
			latitude.append(response_dict['lat'])
			longitude.append(response_dict['lon'])
			#print response.content

	#print city,"\n",latitude,"\n",longitude
	return(city,latitude,longitude)

def createKML(city,longitude,latitude):

	kml = simplekml.Kml(name="TracerouteMap Map", open=1)
	tour = kml.newgxtour(name="Packet Route")
	playlist = tour.newgxplaylist()

	#ploting

	for i in range(len(city)):
		pnt = kml.newpoint(name=city[i])
		pnt.coords = [(longitude[i],latitude[i])]
		pnt.style.labelstyle.color = simplekml.Color.red  # Make the text red
		pnt.style.labelstyle.scale = 3  # Make the text twice as big
		pnt.style.iconstyle.icon.href = 'https://cdn2.iconfinder.com/data/icons/social-media-8/512/pointer.png'
		pnt.style.iconstyle.scale = 2
		flyto = playlist.newgxflyto(gxduration=7)
		flyto.camera.longitude = longitude[i]
		flyto.camera.latitude = latitude[i]
		wait = playlist.newgxwait(gxduration=3)

	#joining

	for i in range(len(city)):
		try:
			name = city[i] + " to " + city[i+1]
			lin = kml.newlinestring(name=name)
			lin.coords=[(longitude[i],latitude[i]), (longitude[i+1],latitude[i+1])]
			lin.style.linestyle.width = 8
			lin.style.linestyle.color = simplekml.Color.cyan
			lin.tessellate = 1
			lin.altitudemode = simplekml.AltitudeMode.clamptoground
		except IndexError:
			pass

		filename="tracemap_of_"+options.host+".kml"
	kml.save(filename)
	return filename

ipaddr=traceroute()
print "[+]TraceRoute Done!!!\n"
#get ip address

print "Getting IP Adress GeoLocation"
data=getlocation()
city=data[0]
latitude=data[1]
longitude=data[2]
print "[+]Done!!!\n"
#get data from ip-api the city,latitude,longitude of IP Adresss

print "Creating KML file !!!"
file=createKML(city,longitude,latitude)
print "[+]Almost Done!!!\n"
#create KML file to view in google earth app

print "[+]Open "+file+" file in Google-Earth"
