# **`CRIE UM MÓDULO QUE SEJA CAPAZ DE FAZER A OPERAÇÃO DE UM BANCO`** 

# **`A PRINCIPIO APENAS SAQUES E DEPOSITO`**

from deposito import deposito
from saque import saque
from menu import menu

menu()

def operation():
    value = 100
    choose = input('Digite a operação: ')

    if choose == "1":
       meu_saque = float(input('Digite o valor: '))
       print('Valor em conta')
       saque(value,meu_saque)
    elif choose =='2':
        meu_deposito = float(input('Digite o valor: '))
        print('Valor em conta R$')
        deposito(value, meu_deposito)
    else:
        print('Escolha uma opção valida')
        operation()


operation()

def loop():
    choose2 = input('Deseja continuiar? S/N')
    print(choose2)
    while choose2 == 'S':
        operation()
    
       