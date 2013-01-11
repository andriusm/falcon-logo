#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
import random

def main():
	fp = open("falcon.bmp", "rb")
	fp.seek(18)
	
	value = fp.read(4)
	width = struct.unpack('I', value)[0]
	value = fp.read(4)
	height = struct.unpack('I', value)[0]
	print "%s x %s" % (width, height)

	x = y = 0
	vertices = 0

	fp.seek(1078)
	i = 0
	while(True):
		if x == width:
			x = 0
			y += 1
			#fp.read(1)
		if y==height:
			break
		x += 1

		value = fp.read(1)
		try:
			color = struct.unpack('B', value)[0]
			if (color < 150):
				vertices += 1
				vx = float( x - (width/2) )
				vy = float( y - (height/2) )
				vz = 5.0 - (random.random() * 10.0)
				print vx, ",", vy, ",", vz, ",",
				if (vertices%10==0):
					print
			#print color
		except:
			print "brake @", fp.tell()
			break
		i += 1

	print
	print "total:", i, "bytes of data"
	print "finished @", fp.tell()
	print "vertices:", vertices

 	fp.close()

if __name__ == '__main__':
	main()