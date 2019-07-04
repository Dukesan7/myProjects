import time

o = 1
loop = 1

while loop == 1:
	s = o = o + o
	p = str(s)
	time.sleep(0.1)
	print(s)
