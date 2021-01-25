from sys import stdin

inp = list(map(str.split, stdin.readlines()[1::]))
a = list(map(int, inp[0]))
b = list(map(int, inp[1]))
# print(inp, a, b)
b.sort()

bl = [0]*len(b)
# DEBUG
# print(bl)

for i in range(len(b)):
    for i2 in a:
        if i2 <= b[i]:
            bl[i] += 1

# DEBUG
# print(bl)
valid = int()


def recurse(ind, pre, sub):
    global valid
    global b
    global bl
    if ind == len(b):
        valid = pre
        return
    new = pre * (bl[ind] - sub)
    recurse(ind + 1, new, sub + 1)


recurse(1, bl[0], 1)
print(valid)
