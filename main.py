print("Hello, world!")
for i in range(10):
	print(i)
	
a = 10
b =15

for i in range (10):
	c = a+b
	
	a = b
	b = c 
	
	print("Число {} равно {}".format(i,c))

