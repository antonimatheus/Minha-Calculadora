# Minha Primeira Calculadora

#importei o sleep para dar uma fluidez ao programa
from time import sleep

nome = str(input('Como você se chama? '))

#boas-vindas <3
print(f'Muito Prazer {nome}, este é o meu primeiro projeto de calculadora!')

#while true para criar um loop para tratar os erros
while True:
    resp = str(input('Gostaria de continuar? s/n ')).upper()
    if resp == 'S':
        
        #usando 'while True' para cada pergunta(input)  
        while True:
            try:
                n1 = float(input('Digite o valor 1: '))
                
            #o 'ValueError' serve para identificar o erro e irá se pedir novamente o que perguntou..
            except ValueError:
                print('\033[31mErro!\033[m Somente números!')
            else:
                break
        
        #usando 'while True' para cada pergunta(input)        
        while True: 
            try:
                n2 = float(input('Digite o valor 2: '))
            except ValueError:
                print('\033[31mErro!\033[m Somente números!')
            else:
                break
                
       
        while True:
            cal = input('Quais desses sinais você irá usar? (+, -, *, /) ')
            
            #caso não seja  (+, -, *, /) nenhuma dessas.. irá se repetir até ser alguma dessas..
            if cal not in '+-*/':
                print('\033[31mErro!\033[m Somente (+, -, *, /)')
            else:
                break
                
        while True:
            perg = str(input('Deseja alterar o cálculo? (s/n) ')).upper()
            if perg == 'N':
                print('Calculando..')
                sleep(1.5)
                
                #para cada símbolo (+, -, *, /) fiz uma repetição para calcular o que foi pedido
                while True:
                    if cal == '+':
                        soma = n1 + n2
                        print(f'A soma de {n1} + {n2} é igual a {soma:.2f}!')
                        break
                    elif cal == '-':
                        subtração = n1 - n2
                        print(f'A subtração de {n1} - {n2} é igual a {subtração:.2f}!')
                        break
                    elif cal == '*':
                        multiplicação = n1 * n2
                        print(f'A multiplicação de {n1} x {n2} é igual a {multiplicação:.2f}!')
                        break
                    elif cal == '/':
                        divisão = n1 / n2
                        print(f'A divisão de {n1} / {n2} é igual a {divisão:.2f}!')
                        break
                break
            else:
                break
                
    elif resp == 'N':
        print('OK! Até a próxima!')
        break
    else:
        print('\033[31mErro!\033[m Somente (s/n) ')
        continue
    
print('Obrigado por vistar o meu código <3')

#feito por @antoniimatheus

    