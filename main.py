#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Bnumb


def usage():
	print "\nfirst argument - first in file\n"
	print "\nsecond argument - operation, if operation is multiplicate use 'x' \n"
	print "\nthird argument - second in file\n"
	print "\nfourth argument - out file\n"
	print "\nfifth argument - [-b] flag, use it if you want work with binary files or [-t] if you want work with text files\n"
	sys.exit(-1);

binaryflag = False;
if len(sys.argv) < 6 or len(sys.argv) > 6:
	usage();
elif len(sys.argv) == 6:
	

	X = Bnumb.Bnumb();
	Y = Bnumb.Bnumb();
	Z = Bnumb.Bnumb();

	if sys.argv[5] == "-b":
		binaryflag = True;
		X.readbin(sys.argv[1]);
		Y.readbin(sys.argv[3]);
	if sys.argv[5] == "-t":
	 	binaryflag == False;
		X.readtxt(sys.argv[1]);
		Y.readtxt(sys.argv[3]);
		
	if sys.argv[2] == "+":
		Z = X + Y;
	elif sys.argv[2] == "-":
		Z = X - Y;
	elif sys.argv[2] == "x":
		Z = X * Y;
	elif sys.argv[2] == "/":
		Z = X / Y;
	elif sys.argv[2] == "%":
		Z = X % Y;
	elif sys.argv[2] == "^":
		Z = X ^ Y;
	else:
		usage();
	if binaryflag == False:
		Z.writetxt(sys.argv[4]);
	else:
		Z.writebin(sys.argv[4]);
