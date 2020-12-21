import sys
inp = list(map(int, sys.stdin.read().split()))
# DEBUG
# print(inp)
# abc = max(inp)
# inp.remove(abc)
a = min(inp)
inp.remove(a)
b = min(inp)
inp.remove(b)
ab = a + b
inp.remove(ab)
c = min(inp)
inp.remove(c)
print(a, b, c)