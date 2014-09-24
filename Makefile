all: 	
	swig -c++ -python Bnumb.i
	g++ -fPIC -c Bnumb.cpp
	g++ -fPIC -c Bnumb_wrap.cxx -I/usr/include/python2.7/
	g++ -shared Bnumb.o Bnumb_wrap.o -o _Bnumb.so
