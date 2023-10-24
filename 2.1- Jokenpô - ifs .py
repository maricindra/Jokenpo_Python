# JOKENPÔ ( usando IF em if , elif e else)
# Uso da bibliotece random
import random

#lista armazenando as opções da partida
opcoes = ["pedra","papel","tesoura"]
print("Bem vindo ao game Jokenpô!\n")

#Rodada entre do usuário
rodada_do_jogador = input("Escolha: Pedra , Papel ou Tesoura \n")

#Por meio da biblioteca random, o computador escolheu
rodada_do_computador = random.choice(opcoes)

#Usuario e computador disputando:
print("\n""Você escolheu ",rodada_do_jogador,"\nO computador escolheu",rodada_do_computador, "\n")

#regras do Jokenpô para resultado: Pedra
if rodada_do_jogador.lower() == "pedra": 
    if rodada_do_computador == "pedra":
        print("EMPATE!")
    elif rodada_do_computador == "papel":
        print("Você perdeu !")
    else: #pc = tesoura
        print("você venceu!") 

#regras do Jokenpô para resultado: Papel
elif rodada_do_jogador.lower() == "papel": 
    if rodada_do_computador=="papel":
        print("EMPATE!")
    elif  rodada_do_computador =="tesoura":
        print("Você perdeu !")
    else: #pc = pedra
        print("você venceu")

#regras do Jokenpô para resultado: Tesoura
elif rodada_do_jogador.lower() == "tesoura": 
    if rodada_do_computador=="tesoura":
        print("EMPATE!")
    elif  rodada_do_computador == "pedra":
        print("Você perdeu !")
    else: #pc = papel
        print("você venceu")

# Orientando novamente o usuário para o menu.
else: print ("Opa! Você digitou outra coisa... ")
