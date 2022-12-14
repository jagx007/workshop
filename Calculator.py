print('\t \t CALCULATOR')


def add():
    x = a + b
    return x


def sub():
    x = a - b
    return x


def mul():
    x = a * b
    return x


def div():
    x = a / b
    return x

def flr():
    x = a // b
    return x

def mod():
    x = a % b
    return x

def pow():
    x = a ** b
    return x


while True:
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    c = int(input('\t1. ADD \n \t2. SUBSTRACT \n \t3. MULTIPLY \n \t4. DIVIDE \n \t5. FLOOR DIVISION \n \t6. MODULUS \n \t7. POWER \n \t enter: '))

    if c == 1:
        print(f'{a} + {b} = ', add())

    elif c == 2:
        print(f'{a} - {b} = ', sub())

    elif c == 3:
        print(f'{a} x {b} = ', mul())

    elif c == 4:
        print(f'{a} / {b} = ', div())
    
    elif c == 5:
        print(f'{a} // {b} = ', flr())
    
    elif c == 6:
        print(f'{a} % {b} = ', mod())

    elif c == 7:
        print(f'{a} ^ {b} = ', pow())

    else:
        print('Syntax error')

    q = input('Do you want to continue(y/n): ')
    if q in 'Nn':
        break
    else:
        continue
