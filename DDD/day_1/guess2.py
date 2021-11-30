import sys

A = [ x for x in range(1000) ]
    
l = 0
r = len(A)

while l < r:
    m = (l + r + 1) // 2
    print(m)
    answer = input()
    if answer == "lower":
        r = m -1
    elif answer == "higher":
        l = m
    else:
        sys.exit()

print(l)
