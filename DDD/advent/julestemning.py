import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip("\n"))
nq = lines[0].split()

# Antal juletræer
n = int(nq[0])

# Antal børn
q = int(nq[1])

lines = lines[1:]

# Smukhedværdier
s = [ int(lines[0].split()[x]) for x in range(n) ]

lines = lines[1:]

lines = [ x.split() for x in lines ]

for i in range(len(lines)):
    for j in range(2):
        lines[i][j] = int(lines[i][j])

print(lines)
print(s)
