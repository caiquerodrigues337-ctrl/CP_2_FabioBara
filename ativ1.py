vogaisref = 'aeiouáàéèêãâíìîóòõôúùû'

vogais=0
consoantes=0

frase=input('digite alguma frase: ').lower()

for caractere in frase:
    if caractere.isalpha():
        if caractere in vogaisref:
         vogais += 1

        else:
           consoantes +=1

print(f'A quantidade de vogais são {vogais}')
print(f'A quantidade de consoantes são {consoantes}')
