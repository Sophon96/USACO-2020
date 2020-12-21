from sys import stdin

n = int(stdin.readline())
north = list()
east = list()
results = ['Infinity' for i in range(n)]
# print(results)

inp = list(map(str.split, stdin.readlines()))
for i in inp:
	if i[0] == 'E':
		east.append((int(i[1]), int(i[2]), int(inp.index(i))))
	else:
		north.append((int(i[1]), int(i[2]), int(inp.index(i))))


# print(north, east)


def xsort(e):
	return e[1]


north.sort()
east.sort(key=xsort)
# print(north, east)
for i in north:
	for i2 in east:
		if i2[0] > i[0] or i[1] > i2[1]:
			continue
		if i2[1] - i[1] > i[0] - i2[0] and results[i[2]] == 'Infinity':
			results[i[2]] = i2[1] - i[1]
			break
		elif i2[1] - i[1] < i[0] - i2[0] and results[i2[2]] == 'Infinity':
			results[i2[2]] = i[0] - i2[0]

for thing in results:
	print(thing)
