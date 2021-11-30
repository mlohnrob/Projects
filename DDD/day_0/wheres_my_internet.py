import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip("\n"))

n = int(lines[0].split()[1])

lines = lines[1:]

parent = [ x for x in range(n) ]

s = [ 1 for i in range(n) ] 

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

if "1" in lines:
    print("Har 1")
else:
    print("Har ikke 1")
    alle = []
    for i in lines:
        for j in i:
            if j != " ":
                alle.append(j)
    print(alle)

    # print([ x + (laveste -1) for x in])

for i in lines:
    pass
