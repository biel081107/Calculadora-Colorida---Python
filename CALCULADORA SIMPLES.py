#CALCULADORA SIMPLES

from MinhasFunções.texto import titulo,menu,linha
from time import sleep

vezes = 0
a = 0
b = 0
while True:
    titulo('CALCULADORA SIMPLES','\033[1;94m')
    opc = ['INSERIR NUMEROS','SOMAR','MULTIPLICAR','DIVIDIR','FINALIZAR EXECUÇÃO']
    menu(opc,'\033[1;93m')
    linha('\033[1;94m',20)
    escolha = int(input(f'\033[1;93mQUAL VOCÊ ESCOLHE: \033[m'))
    if escolha > len(opc) - 1 or escolha < 0:
        print(f'\033[1;31mOPÇÃO INVALIDA, VERIFIQUE O N° DA OPC INSERIDO E TENTE NOVAMENTE\033[m')
    elif escolha != 0 and vezes == 0:
        print(f'\033[1;91mVOCÊ SE ESQUECEU DE INSERIR OS NUMEROS, INSIRA-OS PRIMEIRO\033[m')
        a = float(input('\033[1;97mQUAL VAI SER O 1° NUMERO: '))
        b = float(input('QUAL VAI SER O 2° NUMERO: \033[m'))
        print(f'\033[1;92mNUMEROS FORAM ENVIADOS COM SUCESSO!!!')
    else:
        if escolha == 0:
            a = float(input('\033[1;97mINSIRA UM VALOR PARA O 1° NUMERO: '))
            b = float(input('INSIRA UM VALOR PARA O 2° NUMERO: \033[m'))
            print(f'\033[1;92mNUMEROS FORAM ENVIADOS COM SUCESSO!!!\033[m')
        elif escolha == 1:
            print(f'\033[1;95mA SOMA DOS NUMEROS {a} + {b} É IGUAL A : {a + b:.1f}')
        elif escolha == 2:
            print(f'\033[1;95mA MULTIPLICAÇÃO DOS NUMEROS {a}x{b} É IGUAL A : {a * b:.1f}')
        elif escolha == 3:
            print(f'\033[1;95mA DIVISÃO DOS NUMEROS {a}÷{b} = {a / b:.2f} ou'
                  f' {b}÷{a} = {b / a:.2f}')
        elif escolha == 4:
            print(f'\033[1;92mAGUARDE ALGUNS SEGUNDOS PARA FINALIZARMOS: ', end=' ')
            for c in range(5):
                print(c, end=' ')
                sleep(0.5)
            print(f'FINALIZADO COM SUCESSO!!!\033[m')
            print(f'\033[1;92mMUITO OBRIGADO!! VOLTE SEMPRE\033[m')
            break
    print(f'\033[1;91mAGUARDE ALGUNS SEGUNDOS: ',end=' ')
    for c in range(5):
        print(c,end=' ')
        sleep(0.5)
    print(f'\033[1;31mAPROVEITE!!!')
    sleep(0.5)
    linha('\033[1;92m',20)
    vezes += 1



