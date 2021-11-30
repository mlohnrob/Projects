import sys

said = input()

for i in range(len(said)):
    if i % 2 != 0: continue
    word = said[i:i+2]
    if word != "ho":
        print("der er ugler i mosen")
        sys.exit()
print("den er god nok")
