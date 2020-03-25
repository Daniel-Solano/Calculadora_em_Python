# Calculadora em Python

oper = int(input('Selecione o número da opção desejada: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite sua opção (1/2/3/4): '))

def erro():
    print('Opção inválida')

if oper == 1 or oper == 2 or oper == 3 or oper == 4:

    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')

    def soma(x,y):
        total = float(x) + float(y)
        print(x, ' + ', y, ' = ', total)

    def subt(x,y):
        total = float(x) - float(y)
        print(x, ' - ', y, ' = ', total)

    def mult(x,y):
        total = float(x) * float(y)
        print(x, ' * ', y, ' = ', total)

    def div(x,y):
        total = float(x) / float(y)
        print(x, ' - ', y, ' = ', round(total, 2))

    if oper == 1:
        soma(x,y)
    elif oper == 2:
        subt(x,y)
    elif oper == 3:
        mult(x,y)
    elif oper == 4:
        div(x,y)
          
else:
    erro() 

# Adicionando uma linha nova para testes    
    