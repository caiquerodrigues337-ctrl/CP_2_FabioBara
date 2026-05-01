# Crie um programa com menu interativo (usando while True) que gerencie uma lista de endereços IP. 
# O menu deve ter as opções: 
# [1] Adicionar IP, 
# [2] Remover IP, 
# [3] Listar todos, 
# [4] Buscar IP, 
# [5] Sair. 
# Não permita IPs duplicados na lista. 
# Na busca, informe se o IP foi encontrado e em qual posição.
# Use break para sair do loop quando o usuário escolher a opção 5.

ips = []

while True:
    print("\n--- MENU DE GERENCIAMENTO DE IP ---")
    print("[1] Adicionar IP")
    print("[2] Remover IP")
    print("[3] Listar todos")
    print("[4] Buscar IP")
    print("[5] Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        novo_ip = input("Digite o IP para adicionar: ").strip()
        if novo_ip in ips:
            print(f"Erro: O IP {novo_ip} já está na lista.")
        else:
            ips.append(novo_ip)
            print(f"IP {novo_ip} adicionado com sucesso!")

    elif opcao == '2':
        ip_remover = input("Digite o IP que deseja remover: ").strip()
        if ip_remover in ips:
            ips.remove(ip_remover)
            print(f"IP {ip_remover} removido com sucesso.")
        else:
            print("Erro: Este IP não consta na lista.")

    elif opcao == '3':
        if not ips:
            print("\nA lista de IPs está vazia.")
        else:
            print("\n--- LISTA DE IPs ---")
            for i, ip in enumerate(ips):
                print(f"{i}: {ip}")

    elif opcao == '4':
        ip_busca = input("Digite o IP que deseja buscar: ").strip()
        if ip_busca in ips:
            posicao = ips.index(ip_busca)
            print(f"O IP {ip_busca} foi ENCONTRADO na posição {posicao}.")
        else:
            print(f"O IP {ip_busca} NÃO foi encontrado na lista.")

    elif opcao == '5':
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")