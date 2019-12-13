import os.path
path1="./Output/"
pathname=os.path.join(path1,filename+"_data"+".txt")
outF = open(pathname, "w")
outF.write(fff)
outF.close()
str="\n"
abstractinfo=abstract.split(".")
for i in abstractinfo:
	if(i!=""):
		str = str + '@label\n' + i+"\n";
with open(pathname, "a") as myfile:
	myfile.write(str)

myfile.close()