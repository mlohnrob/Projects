import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip("\n"))
nm = lines[0].split()
n = int(nm[0])
m = int(nm[1])

lines = lines[1:]

buckets = [ int(x) for x in lines[:n] ]
buckets.sort()
paints = [ int(x) for x in lines[n:n+m] ]


def binary_search(A, element):
    
    def S(cnt):
        if cnt == 0: return True
        else: return A[cnt-1] < element

    l = 0
    r = len(A)

    while l < r:
        m = (l + r + 1) // 2
        if S(m): l = m
        else: r = m - 1

    print(l)
    return l < len(A) and A[l] == element

for p in paints:
    print(binary_search(buckets, p))
