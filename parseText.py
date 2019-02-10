import re
import numpy as np

lines = []
with open('new.txt', 'rt') as in_file:
    for line in in_file:
        lines.append(line.rstrip('\n'))

lines1 = []
rows = []
for line in lines:
    label = int(re.split(':', line)[0])

    filtered = re.split('1:', line)[1].strip()
    filtered = filtered.replace("[", "")
    filtered = filtered.replace("]", "")
    hi = filtered.split(',')
    newArr = [float(el) for el in hi]
    el = [label] + newArr
    lines1.append(el)
mylines = np.asarray(lines1)
print(mylines[:, 0])
print(mylines[1, 1:])
print(mylines.shape[0])
print(mylines.shape[1])
myrand = np.random.random_sample((256 * 3) + 1,)
# print(myrand)
# print(myrand[0])
# print(myrand.shape)


