import random
import string

cofre_senhas = {}

def avaliar_forca(senha):
    tem_maiuscula = False
    tem_numero = False
    tem_simbolo = False
    
    for char in senha:
        if char in string.ascii_uppercase: tem_maiuscula = True
        if char in string.digits: tem_numero = True
        if char in string.punctuation: tem_simbolo = True
    
    pontuacao = sum([len(senha) >= 8, tem_maiuscula, tem_numero, tem_simbolo])
    
    if pontuacao <= 1: return "Fraca"
    elif pontuacao <= 3: return "Média"
    else: return "Forte"

while True:
    print("\n" + "="*30)
    print("  GERENCIADOR DE SENHAS PRO")
    print("="*30)
    print("[1] Cadastrar Senha\n[2] Listar Serviços\n[3] Buscar Senha\n[4] Gerar Senha Aleatória\n[5] Avaliar Todas as Senhas\n[6] Exportar Relatório\n[7] Sair")
    
    opcao = input("\nEscolha uma opção: ")

    try:
        if opcao == '1':
            servico = input("Nome do serviço (ex: Gmail): ").strip().capitalize()
            if servico in cofre_senhas:
                raise ValueError("Este serviço já possui uma senha cadastrada!")
            
            senha = input("Digite a senha: ")
            forca = avaliar_forca(senha)
            cofre_senhas[servico] = senha
            print(f"[✔] Senha cadastrada! Força: {forca}")

        elif opcao == '2':
            if not cofre_senhas:
                print("Cofre vazio.")
            else:
                print("\nServiços cadastrados:")
                for s in cofre_senhas.keys():
                    print(f"- {s}")

        elif opcao == '3':
            servico = input("Buscar qual serviço? ").strip().capitalize()
            if servico in cofre_senhas:
                print(f"Senha de {servico}: {cofre_senhas[servico]}")
            else:
                print("Serviço não encontrado.")

        elif opcao == '4':
            tamanho = int(input("Tamanho da senha desejada: "))
            if tamanho < 4: raise ValueError("Tamanho mínimo é 4.")
            
            caracteres = string.ascii_letters + string.digits + string.punctuation
            senha_gerada = ""
            for _ in range(tamanho):
                senha_gerada += random.choice(caracteres)
            
            print(f"\nSenha sugerida: {senha_gerada}")
            print("Dica: Use-a no cadastro (Opção 1).")

        elif opcao == '5':
            if not cofre_senhas:
                print("Nada para avaliar.")
            else:
                print(f"\n{'SERVIÇO':<15} | {'CLASSIFICAÇÃO'}")
                print("-" * 30)
                for serv, sen in cofre_senhas.items():
                    print(f"{serv:<15} | {avaliar_forca(sen)}")

        elif opcao == '6':
            try:
                with open("relatorio_senhas.txt", "w") as arquivo:
                    arquivo.write("RELATÓRIO DE SEGURANÇA\n" + "="*22 + "\n")
                    for serv, sen in cofre_senhas.items():
                        arquivo.write(f"Serviço: {serv} | Força: {avaliar_forca(sen)}\n")
                print("[✔] Relatório 'relatorio_senhas.txt' gerado com sucesso!")
            except Exception as e:
                print(f"Erro ao salvar arquivo: {e}")

        elif opcao == '7':
            print("Encerrando sistema com segurança...")
            break

        else:
            print("Opção inválida!")

    except ValueError as e:
        print(f"Erro de entrada: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")