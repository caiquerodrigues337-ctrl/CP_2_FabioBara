# Crie um programa que receba as notas de 5 alunos (nome e nota) e 
# armazene cada par como uma tupla dentro de uma lista. 
# Depois, usando laços, 
# calcule e exiba:
# a maior nota e o nome do aluno, 
# a menor nota e o nome do aluno, 
# a média da turma, 
# e quais alunos estão acima da média. 
# Use for para percorrer a lista.

alunos = []

for i in range(5):
    print(f"--- Registro do {i+1}º Aluno ---")
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    
    alunos.append((nome, nota))

maior_nota = alunos[0]  
menor_nota = alunos[0]  
soma_notas = 0


for aluno in alunos:
    nome, nota = aluno  
    soma_notas += nota
    
    if nota > maior_nota[1]:
        maior_nota = aluno
        
    if nota < menor_nota[1]:
        menor_nota = aluno


media_turma = soma_notas / 5


print("-" * 30)
print(f"Maior nota: {maior_nota[1]} (Aluno: {maior_nota[0]})")
print(f"Menor nota: {menor_nota[1]} (Aluno: {menor_nota[0]})")
print(f"Média da turma: {media_turma:.2f}")
print("-" * 30)

print("Alunos acima da média:")
for aluno in alunos:
    if aluno[1] > media_turma:
        print(f"- {aluno[0]} (Nota: {aluno[1]})")