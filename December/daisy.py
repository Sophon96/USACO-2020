from sys import stdin
from statistics import mean
n = int(stdin.readline().strip())
inp = list(map(int, stdin.readline().split()))
# DEBUG
# print(n)
# print(inp)

# Add n to the count, as shown in the example
count = n
for i in range(n):
	for i2 in range(i + 1, n):
		# DEBUG
		# print(i, i2, count)
		avg = mean(inp[i:i2 + 1])
		if inp[i:i2 + 1].count(avg):
			count += 1
		# DEBUG
		# print(i, i2)
print(count)
