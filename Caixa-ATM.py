import os
import time

saldo = 1200.00

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n" + "="*24)
    print("-----Menu Principal-----")
    print("="*24)
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

opcao = -1

while opcao != 0:
    limpar_tela()
    exibir_menu()

    try:
        opcao = int(input("Escolha a opção que deseja: "))

        if opcao == 1: 
            print("\n" + "="*24)
            print(f"Seu Saldo e {saldo:.2f}")
            print("="*24)
            time.sleep(2)

        elif opcao == 2:
            print("\n" + "="*24)
            valor = float(input("Qual valor deseja depositar?: R$"))
            saldo += valor
            print(f"O valor depositado {valor} ja foi adicionado")
            print(f"O seu novo saldo e de {saldo:.2f}")
            print("="*24)
            time.sleep(2)

        elif opcao == 3:
            print("\n" + "="*24)
            print(f"O seu saldo e de {saldo:.2f} quanto deseja sacar")
            print("="*24)
            valor_saque = float(input("Quanto voce deseja sacar; R$ "))
            
            
            if valor_saque <= 0:
                print("\n" + "="*24)
                print("O valor deve ser maior que zero!!!!")
                print("="*24)

            elif valor_saque <= saldo:
                saldo -= valor_saque
                print("\n" + "="*24)
                print(f"Saque de R${valor_saque} foi feito com sucesso")
                print(f"Novo saldo disponivel R${saldo:.2f}")
                print("="*24)
            else:
                print("\n" + "="*24)
                print("O seu saldo e insuficiente para realizar o seu saque!!")
                print("="*24)
            time.sleep(2)

        elif opcao == 0:
            print("\n" + "="*24)
            print("Encerrando o sistema!!!")
            print("="*24)
            time.sleep(1)

        else:
            print("\n" + "="*24)
            print("Opçao Invalida! Escolha entre 0 e 3")
            print("="*24)
            time.sleep(1)

    except ValueError:
        print("\n" + "="*24)
        print("Erro: Digite apenas numeros")
        print("="*24)
        time.sleep(2)
        limpar_tela()

print("Programa encerrado")
