#!/usr/bin/env python3
import matplotlib.pyplot as plt
from integer import Integer
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))
def main():
#C++
	f = Integer(47)
	print(f.fib())
	#f.set(7)
	#print(f.fib())

#python
	#print(fib_py(6))

#tidtagning
	a = 30
	py = []
	inte = []
	while a < 45:
		startpy = pc()
		fib_py(a)
		endpy = pc()
		py.append(endpy-startpy)
		f = Integer(a)
		startit = pc()
		f.fib()
		endit = pc()
		inte.append(endit-startit)
		a += 1

	x = list(range(30,45))
	plt.plot(x,py,'r',x,inte,'b')
	plt.savefig('plott.png')

if __name__=='__main__':
	main()
