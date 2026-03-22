saldo = 1200.00

def exibir_menu():
    print("\n" + "="*20)
    print("-----Menu Principal-----")
    print("="*20)
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

opcao = -1

while opcao != 0:
    exibir_menu()

    try:
        opcao = int(input("Escolha a opção que deseja: "))

        if opcao == 1: 
            print(f"Seu Saldo e {saldo:.2f}")

        elif opcao == 2:
            valor = float(input("Qual valor deseja depositar?"))
            saldo += valor
            print(f"O valor depositado {valor} ja foi adicionado")
            print(f"O seu novo saldo e de {saldo:.2f}")

        elif opcao == 3:
            print(f"O seu saldo e de {saldo:.2f} quanto deseja sacar")
            valor_saque = float(input("Quanto voce deseja sacar; R$ "))
            
            if valor_saque <= 0:
                print("O valor deve ser maior que zero!!!!")

            elif valor_saque <= saldo:
                saldo -= valor_saque
                print(f"Saque de R${valor_saque} foi feito com sucesso")
                print(f"Novo saldo disponivel R${saldo:.2f}")
            else:
                print("O seu saldo e insuficiente para realizar o seu saque!!")

        elif opcao == 0:
            print("Encerrando o sistema!!!")

        else:
            print("Opçao Invalida! Escolha entre 0 e 3")

    except ValueError:
        print("Erro: Digite apenas numeros")

print("Programa encerrado")

