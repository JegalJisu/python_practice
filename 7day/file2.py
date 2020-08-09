testFile = open('test.txt')
inp = testFile.read()

print(len(inp))
print(inp[:20])

for cheese in testFile :
    print(cheese)

testFile.seek(0)
for cheese in testFile :
    print(cheese)
testFile.close()