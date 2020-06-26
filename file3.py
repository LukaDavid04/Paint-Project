#file3.py
from random import*
outfile=open("nums.txt","w")
for i in range(10000):
	outfile.write("%d/t"%randint(0,1000))
	outfile.close()