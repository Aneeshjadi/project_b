matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
	for j in range(0,3):
		print(matrix[i][j],end=" ")
	print()
sum=0
for i in range (0,3):
	for j in range(0,3):
		sum=sum+matrix[i][j]

print("sum of elements",sum)


sum=0
for i in range (0,3):
	for j in range(0,3):
		if(i==j):
			sum=sum+matrix[i][j]

print("sum of dia elements",sum)

sum=0
for i in range(0,3):
	for j in range(0,3):
		if(i+j==2):
			sum=sum+matrix[i][j]
print("sum of rev dia elements",sum)