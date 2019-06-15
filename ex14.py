a = input('vedite slovo: ')
b = input('vedite simvol: ')
print('Otvet:')
if a == '':
    print('Pustaya stroka')
else:
    print("Perviy index " , a.find(b))
    print("Posledniy index " , a.rfind(b))
