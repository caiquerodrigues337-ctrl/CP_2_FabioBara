while True:
    print("\n" + "="*20)
    print("CALCULADORA SEGURA")
    print("="*20)
    print("Digite 'sair' a qualquer momento para encerrar.")

    try:
        entrada1 = input("Primeiro número: ").strip().lower()
        if entrada1 == 'sair': break
        num1 = float(entrada1)

        operacao = input("Operação (+, -, *, /): ").strip()
        if operacao == 'sair': break

        entrada2 = input("Segundo número: ").strip().lower()
        if entrada2 == 'sair': break
        num2 = float(entrada2)

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2 
        else:
            raise ValueError("Operação inválida! Use apenas +, -, * ou /.")

    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Erro: Por favor, digite apenas números válidos.")
        else:
            print(f"Erro: {e}")

    except ZeroDivisionError:
        print("Erro: Matemática básica! Não é possível dividir por zero.")

    else:
        print(f"\n>>> Resultado: {num1} {operacao} {num2} = {resultado}")

    finally:
        print("Operação processada.")

print("\nObrigado por usar a calculadora! Até logo.")