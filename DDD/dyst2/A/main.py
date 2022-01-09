inp = input().split()

volume = int(inp[0]) * int(inp[1]) * int(inp[2])

nr_snblde = volume // 500

if volume - 500 * nr_snblde > 200:
    vasker = "ja"
else: 
    vasker = "nej"

print(nr_snblde)
print(vasker)
