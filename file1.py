#file1
infile=open("names.txt","r")
names=infile.readlines()
for name in names:
	print("Hello",name)
infile.close()