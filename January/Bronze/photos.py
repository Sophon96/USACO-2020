from sys import stdin

inp = list(map(int, stdin.readlines()[1].split()))
# DEBUG
inp.sort()
# print(inp)

count = 0
for i in range(len(inp)):
    if len(inp) == 0:
        break
    if not i % 2:
        a = -1
        for i2 in inp:
            if not i2 % 2:
                a = i2
                break
        if a == -1:
            if len(inp) >= 2:
                # print('Before', inp)
                inp.pop(0)
                inp.pop(0)
                # print('After ', inp)
                count += 1
            else:
                count -= 1
                break
        else:
            inp.remove(a)
            count += 1
    elif len(inp):
        a = -1
        for i2 in inp:
            if i2 % 2:
                a = i2
                break
        if a != -1:
            inp.remove(a)
            count += 1
        else:
            break
print(count)
