#!/usr/bin/python2.7
import scapy.all as scapy
import argparse

print "TraceRoute POC"

parser=argparse.ArgumentParser()
parser.add_argument("-i","--host",dest="host",help="Give Hostname or IP Address")
parser.parse_args()
options=parser.parse_args()

print "Host:",options.host

ip=open("ip.txt","w")
ip_addr=[]
for i in range(1,50):
	icmp=scapy.IP(dst=options.host,ttl=i)/scapy.ICMP()
	b=scapy.sr1(icmp,timeout=3,verbose=False)
	if i==1:
		src_ip=b.dst
		print "\nSource_IP:%s\n"%src_ip


	if b is None:
		print "TTL=%s \t*****Router Drops the packet*****"%i
	else:
		if b.src in ip_addr:
			dst_ip=b.src
			print "\nDestination_IP:%s"%dst_ip
			break

		print "TTL=%s \tIntermediate_IP=%s"%(i,b.src)
		ip_addr.append(b.src)
		ip.write(b.src+"\n")

ip.close()
#print ip_addr

