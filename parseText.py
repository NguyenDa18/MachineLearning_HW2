import re

lines = []
with open('parseTest.txt', 'rt') as in_file:
    for line in in_file:
        lines.append(line.rstrip('\n'))

lines1 = []
for line in lines:
    filtered = re.split('1:', line)[1].strip()
    newStr = filtered.replace("[", "")
    newStr2 = newStr.replace("]", "")
    hi = newStr2.split(',')
    newArr = [float(el) for el in hi]
    lines1.append(newArr)
print(lines1)

