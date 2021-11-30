import fileinput

all_gnomes = []
for line in fileinput.input():
    all_gnomes.append(line.strip("\n"))

for i, j in enumerate(all_gnomes):
    if i == 0:
        continue

    j = j.split()
    og = 0
    for k, h in enumerate(j):
        if k == 0:
            continue
        if k == 1:
            og = int(h)
            continue
        if int(h) != og + 1:
            print(k)
        else:
            og = int(h)
