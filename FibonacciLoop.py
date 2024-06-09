# Python program to generate Fibonacci series based on n value
n = int(input())
a = 0
b = 1
sum = a + b
count = 1
print("Fibonacci series is: ", end=" ")
while (count <= n):
	count += 1
	print(a, end=" ")
	a = b
	b = sum
	sum = a + b