import re

lines = []
with open('parseTest.txt', 'rt') as in_file:
    for line in in_file:
        lines.append(line.rstrip('\n'))

lines1 = []
rows = []
for line in lines:
    rows.append(int(re.split(':', line)[0]))
    filtered = re.split('1:', line)[1].strip()
    newStr = filtered.replace("[", "")
    newStr2 = newStr.replace("]", "")
    hi = newStr2.split(',')
    newArr = [float(el) for el in hi]
    lines1.append(newArr)
print(lines1)
print(type(rows[0]))

