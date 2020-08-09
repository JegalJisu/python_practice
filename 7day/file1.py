testFile = open('test.txt', 'r')
count = 0

print(testFile)
for cheese in testFile :
    print(cheese)
    count = count + 1

print("Line count :", count)
print(testFile.read())
testFile.close()