import matplotlib.pyplot as plt
import sys
a=1
x=[]
y=[]
f=open("read.txt","r")
x1=f.read()
x1=x1.split(" ")
for i in x1:
	y.append(int(i))
	x.append(a)
	a+=1
f.close()
plt.plot(x,y)
plt.plot(x,y,"ro")
plt.xticks(x)
plt.yticks(y)
plt.xlabel('Number')
plt.ylabel('Square')
plt.grid()
plt.title("GCI-MakeFile-Demo(Square Numbers)")
plt.show()