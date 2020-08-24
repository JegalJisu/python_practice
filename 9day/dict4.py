counts = {'chuck': 1, 'fred': 42, 'jan': 100, 'nan': 'test', 1: 'abc'}
for key in counts:
    print(key, counts[key])

for key, value in counts.items():
    print(key, value)