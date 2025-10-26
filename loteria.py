import random
import time
jogadores = []


qnts = int(input("Quantidade de competidores: "))
i = 0
while i < qnts:
    
    nome = input(f"Qual o nome do {i+1}° jogador: ")
    numeros = []
    contador = 0
    while contador < 9:
        num = int(input(f"Digite o {contador +1}° numero: "))
        numeros.append(num)
        contador += 1
    jogador = {'nome': nome,  'numeros': numeros, 'acertos': 0}
    jogadores.append(jogador)
    i += 1
i = 0
numeros_aleatorios= random.sample(range(1,100), 10)

for jogador in jogadores:
    for numero in jogador['numeros']:
        if numero in numeros_aleatorios:
            jogador['acertos'] +=1

maior_acerto = 0

for jogador in jogadores:
    if jogador['acertos'] > maior_acerto:
        maior_acerto = jogador['acertos']

ganhadores = []
for jogador in jogadores:
    if jogador['acertos'] == maior_acerto:
        ganhadores.append(jogador['nome'])
        ganhador = jogador['nome']

indice = 0

while indice < len(numeros_aleatorios):
    print ("\n\n\nSorteando...")
    time.sleep(3)
    print (f"{indice+1}° numero sorteado: {numeros_aleatorios[indice]}.")
    for jogador in jogadores:
        if numeros_aleatorios[indice] in jogador['numeros']:
            print (f"{jogador['nome']} acertou esse numero!")
            
    indice += 1
print (f"\n\n\nOs numeros sorteados foram: {', '.join(sorted(map(str, numeros_aleatorios)))}!")
if len(ganhadores) == 1:
    print (f"O ganhador foi {ganhador}! Parabéns!")

else:
    print (f"Houve um empate entre os jogadores: {', '.join(ganhadores)}! Parabéns a eles!")
    
print (f"#Pontuação#")
for jogador in jogadores:
    print (f"{jogador['nome']}: {jogador['acertos']} ponto(s)")
