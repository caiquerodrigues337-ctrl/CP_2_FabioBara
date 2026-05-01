ativos = []

def limpar_ip(ip):
    return ip.strip()

while True:
    print("\n" + "="*35)
    print("  SISTEMA DE INVENTÁRIO DE REDE")
    print("="*35)
    print("[1] Cadastrar Ativo")
    print("[2] Listar Ativos")
    print("[3] Buscar por IP")
    print("[4] Alterar Status")
    print("[5] Remover Ativo")
    print("[6] Sair")
    
    opcao = input("\nEscolha uma opção: ")

    try:
        if opcao == '1':
            nome = input("Nome do dispositivo: ").strip()
            tipo = input("Tipo (Servidor/Estação/Switch/Roteador): ").strip().capitalize()
            ip = limpar_ip(input("Endereço IP: "))
            
            for a in ativos:
                if a['ip'] == ip:
                    raise Exception(f"Erro: O IP {ip} já está cadastrado para o ativo '{a['nome']}'.")
            
            status = input("Status (Ativo/Inativo): ").strip().capitalize()
            
            novo_ativo = {
                "nome": nome,
                "tipo": tipo,
                "ip": ip,
                "status": status
            }
            ativos.append(novo_ativo)
            print("\n[✔] Ativo cadastrado com sucesso!")

        elif opcao == '2':
            if not ativos:
                print("\nInventário vazio.")
            else:
                print(f"\n{'NOME':<15} | {'TIPO':<10} | {'IP':<15} | {'STATUS'}")
                print("-" * 55)
                for a in ativos:
                    print(f"{a['nome']:<15} | {a['tipo']:<10} | {a['ip']:<15} | {a['status']}")

        elif opcao == '3':
            ip_busca = limpar_ip(input("Digite o IP para busca: "))
            encontrado = False
            for a in ativos:
                if a['ip'] == ip_busca:
                    print(f"\nAtivo Encontrado: {a['nome']} ({a['tipo']}) - Status: {a['status']}")
                    encontrado = True
                    break
            if not encontrado:
                raise ValueError("Ativo não encontrado com este IP.")

        elif opcao == '4':
            ip_busca = limpar_ip(input("Digite o IP do ativo para alterar status: "))
            alterado = False
            for a in ativos:
                if a['ip'] == ip_busca:
                    novo_status = "Inativo" if a['status'] == "Ativo" else "Ativo"
                    a['status'] = novo_status
                    print(f"\n[!] Status de '{a['nome']}' alterado para {novo_status}.")
                    alterado = True
                    break
            if not alterado:
                raise ValueError("Não foi possível alterar: IP não localizado.")

        elif opcao == '5':
            ip_busca = limpar_ip(input("Digite o IP do ativo a remover: "))
            removido = False
            for i in range(len(ativos)):
                if ativos[i]['ip'] == ip_busca:
                    print(f"\n[!] Removendo ativo: {ativos[i]['nome']}")
                    ativos.pop(i)
                    removido = True
                    break
            if not removido:
                raise ValueError("Remoção falhou: IP não encontrado.")

        elif opcao == '6':
            print("Encerrando sistema...")
            break
        
        else:
            print("Opção inválida!")

    except Exception as erro:
        print(f"\nALERTA: {erro}")