n=int(input("enter any number"))
x=0
for i in range (1,n+1):
	for j in range (1,i+1):
		x=x+1
		print(x,end=" ")
	print()