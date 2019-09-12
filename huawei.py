raw = input().split("},")

arr1, arr2, r = raw[0][3:].split(','), raw[1][3:].split(','), raw[2][2]

l1 = list(map(int, arr1))
l2 = list(map(int, arr2))
d = int(r)

res = []

p1 = 0
p2 = 0
while p1 < len(l1) and p2 < len(l2):
    if l2[p2] - l1[p1] >= d or l1[p1] <= l2[p2]:
        res.append((l1[p1], l2[p2]))
        p1 += 1
        p2 += 1
    else:
        p2 += 1


print(" ".join([str(x) for x in res]))
