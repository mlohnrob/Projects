import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip("\n"))

n = int(lines[0].split()[0])

lines = lines[1:]

parent = [ x for x in range(n) ]

s = [1 for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return
    if s[py] < s[px]:
        py, px = px, py
    parent[px] = py
    s[py] += s[px]


for i in lines:
    i = i.split()
    if i[0] == "?":
        if find(int(i[1])) == find(int(i[2])):
            print("yes")
        else:
            print("no")
    else:
        union(int(i[1]), int(i[2]))
