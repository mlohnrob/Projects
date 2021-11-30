import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip("\n"))

n = int(lines[0])

lines = lines[1:]

heights = [ int(lines[x]) for x in range(n) ]
heights_sorted = [ heights[x] for x in range(n) ]
heights_sorted.sort()

for i, h in enumerate(heights):
    if h == heights_sorted[-2]:
        print(i+1)
