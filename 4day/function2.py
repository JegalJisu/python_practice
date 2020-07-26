def greet (lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    elif lang == 'ko' :
        return '안녕'
    else :
        return 'Hello'

print(greet('en'))
print(greet('es'))
print(greet('fr'))
print(greet('ko'))