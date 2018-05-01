# -*- coding: utf-8 -*-
import dpkt
import sys
import urllib
import socket
from collections import Counter
file_name = sys.argv[1]
f = open(file_name)
pcap = dpkt.pcap.Reader(f)
dic_src = Counter()
dic_dst = Counter()
for ts,buf in pcap:
	try:	
		eth = dpkt.ethernet.Ethernet(buf)
		ip = eth.data
		tcp = ip.data
		if tcp.flags == 0x002:
			dic_src[ip.src] += 1
		elif tcp.flags == 0x012:
			dic_dst[ip.dst] += 1
	except Exception:
		sys.exc_clear()
		pass

for i in dic_src:
	x = dic_dst[i]
	y = 3*x
	if dic_src[i] > y:
		print socket.inet_ntoa(i)