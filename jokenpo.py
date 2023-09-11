import random

def ganha(jogador, computador):
if(jogador == '1' and computador == '3') or (jogador == '3' and computador == '2') or (jogador == '2'and computador == '1'):
return True

def converter(jogada):
if(jogada == '1'):
return "Pedra"
elif (jogada == '2'):
return "Papel"
else:
return "Tesoura"

jogada_jogador = input("Escolha um para jogar!\n [1]->Para Pedra \n [2]->Para Papel \n [3]->Para Tesoura \n Escolha:")

while int(jogada_jogador) > 3 or int(jogada_jogador) < 1:
print("Digite novamente!")
jogada_jogador = input("Escolha um para jogar!\n [1]->Para Pedra \n [2]->Para Papel \n [3]->Para Tesoura \n Escolha:")

jogada_computador = random.choice(['1', '2', '3'])

print(" Você:", converter(jogada_jogador))
print(" CPU:", converter(jogada_computador))

if jogada_jogador == jogada_computador:
print(" Empatou!")
elif ganha(jogada_jogador, jogada_computador):
print("Você Ganhou!")
else:
print("Você Perdeu!")
