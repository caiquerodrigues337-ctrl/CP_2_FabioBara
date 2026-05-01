# Crie um programa que peça uma senha ao usuário repetidamente (usando while) até que ela atenda TODOS os critérios:
# mínimo 8 caracteres, 
# pelo menos 1 letra maiúscula, 
# pelo menos 1 letra minúscula,
# pelo menos 1 número e 
# pelo menos 1 caractere especial (!@#$%&*).
# A cada tentativa inválida, informe quais critérios não foram atendidos. 
# Use break para sair quando a senha for válida.



especial = '!@#$%&*'



print('==========VALIDADOR DE SENHAS==========')

while True:
    erro = []

    senha = input('DIGITE A SENHA: ')
    # tem_maiuscula = False
    # tem_minuscula = False
    # tem_numero = False
    # tem_especial = False
    if len(senha) < 8:
        erro.append('Mínimo 8 caracteres')
    if not any(char.isupper() for char in senha):
        erro.append('Tem que ter pelo menos uma letra maiuscula')
    elif not any(char.islower() for char in senha):
        erro.append('Tem que ter pelo menos uma letra minuscula')
    elif not any(char.isnumeric() for char in senha):
        erro.append('Tem que ter pelo menos um número')
    elif not any(char in especial for char in senha):
        erro.append(f'Tem que ter pelo menos um caractere especial {especial}')
        print('=====Senha inválida!=====\nCorrija os seguintes pontos:')
    if not erro:
        print("Senha válida!")
        break
    else:
        print("Senha inválida! \nCorrija os seguintes pontos:")
        for o in erro:
            print(f"  - {o}")