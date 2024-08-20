from frota import *

def operar_carro(carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))
    tanque = float(input("Digite a gasolina do tanque: "))
    consumo = float(input("Digite o consumo de gasolina: "))
    motor = False

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor, tanque, consumo)

    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))
    tanque = float(input("Digite a gasolina do tanque: "))
    consumo = float(input("Digite o consumo de gasolina: "))
    motor = False

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor, tanque, consumo)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 300 and carro2.odometro < 300 and (carro1.tanque > 0 or carro2.tanque > 0):
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Escolha um carro para operar [1-2]: "))
            if(op == 1):
                operar_carro(carro1)
            else:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)
    print('Parar para trocar óleo!!!')

