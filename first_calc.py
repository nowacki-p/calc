#'''  First Calculator   '''

x = float(input('Insert the first number: '))
y = float(input('Insert the second number: '))
z = input('What type of operator you want to use(+,-,*,/,**)')
operators ={'+':x+y,'-':x-y,'*':x*y,'/':x/y,'**':x**y}
if z == '+':
    print(operators['+'])
elif z == '-':
    print(operators['-'])
elif z == '*':
    print(operators['*'])
elif z == '/':
    print(operators['/'])
elif z == '**':
    print(operators['**'])
else:
    print("Error- operator not found,\n use designed operator and try again")
    
