import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip("\n"))

n = int(lines[0])

lines = [ x.split() for x in lines[1:] ]

for i, t in enumerate(lines):
    for j, k in enumerate(t):
        lines[i][j] = int(k)

intervals = []

g = 0

for i in lines:
    print(i)
    a = i[0]
    b = i[1]

    if intervals == []:
        intervals.append([a, b])
        g += 1
    else:
        for k in intervals:
            if a < k[0] and b < k[1] and b > k[0]:
                k[0] = a
            elif a > k[0] and b > k[1] and a < k[1]:
                k[1] = b
            elif a == k[0] or b == k[1] or a == k[1] or b == k[0]:
                print(f"hej k: {k}, a: {a}, b: {b}")
                continue
            elif (a < k[0] and b < k[0]) or (a > k[1] and b > k[1]):
                print(f"igen k: {k}")
                if [a, b] not in intervals:
                    print(k[0], k[1])
                    intervals.append([a, b])
                    g += 1

print(intervals)
print(g)
