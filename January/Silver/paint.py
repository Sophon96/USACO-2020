from sys import stdin

inp = stdin.readlines()
n, q = map(int, inp[0].split())
# DEBUG
# print(n, q)

pattern = inp[1]
abc = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
        }
for i in range(q):
    tmp = tuple(map(int, inp[i + 2].split()))
    tmp2 = pattern[0:tmp[0] - 1].strip()
    tmp3 = pattern[tmp[1]:].strip()
    # print(tmp3)
    prev = -1
    count1 = 0
    for i2 in range(len(tmp2)):
        cur = abc[tmp2[i2].lower()]
        if cur > prev:
            count1 += 1
        elif cur < prev:
            mark = False
            rtmp2 = tmp2[::-1]
            for i3 in rtmp2[len(tmp2) - i2::]:
                if abc[i3.lower()] < cur:
                    break
                elif i3 == tmp2[i2]:
                    mark = True
                    break
            if mark:
                pass
            else:
                count1 += 1
                # continue
        prev = cur
    prev = -1
    for i2 in range(len(tmp3)):
        cur = abc[tmp3[i2].lower()]
        if cur > prev:
            # print(0)
            count1 += 1
        elif cur < prev:
            # print(1)
            mark = False
            rtmp3 = tmp3[::-1]
            for i3 in rtmp3[len(tmp3) - i2::]:
                # print(f'i3: {i3}')
                if abc[i3.lower()] < cur:
                    break
                elif i3 == tmp3[i2]:
                    # print(i3)
                    mark = True
                    break
            if not mark:
                # print(3)
                count1 += 1
        prev = cur
    print(count1)
