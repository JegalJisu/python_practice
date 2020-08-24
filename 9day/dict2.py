counts1 = dict()
counts2 = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts1:
        counts1[name] = 1
    else:
        counts1[name] = counts1[name] + 1

for name in names:
    counts2[name] = counts2.get(name, 0) + 1
print(counts1)
print(counts2)