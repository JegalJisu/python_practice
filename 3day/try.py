rawstr = input('Enter a number : ')

try :
    ival = int(rawstr)
except ValueError:
    ival = -1
except Exception as e:
    ival = 0
    print(e)

if ival > 0 :
    print('Nice work')
elif ival == 0 :
    print('Except')
else :
    print('Not a number')