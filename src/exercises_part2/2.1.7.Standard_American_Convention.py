line_SAC = line = input()

for i in range(len(line)-3, 0, -1):
    if (len(line) - i) % 3 == 0:
        line_SAC = line_SAC[:i] + ',' + line_SAC[i:]

print(line_SAC)