# JOKENPÔ ( usando IF em if , elif e else)
import random

opcoes = "pedra","papel","tesoura"
print("Bem vindo ao game Jokenpô!\n")

rodada_do_jogador = input("Escolha: Pedra , Papel ou Tesoura \n")
rodada_do_computador = random.choice(opcoes)

print("\n""Você escolheu ",rodada_do_jogador,"\n""O computador escolheu ",rodada_do_computador)

if rodada_do_jogador.lower() == "pedra": 
    if rodada_do_computador == "pedra":
        print("EMPATE!")
    
    elif rodada_do_computador == "papel":
        print("Você perdeu !")

    else: #pc = tesoura
        print("você venceu!") 

elif rodada_do_jogador.lower() == "papel": 
    if rodada_do_computador=="papel":
        print("EMPATE!")
    
    elif  rodada_do_computador =="tesoura":
        print("Você perdeu !")

    else: #pc = pedra
        print("você venceu")

elif rodada_do_jogador.lower() == "tesoura": 
    if rodada_do_computador=="tesoura":
        print("EMPATE!")
    
    elif  rodada_do_computador == "pedra":
        print("Você perdeu !")

    else: #pc = papel
        print("você venceu")

else: print ("Opa! Você digitou outra coisa... ")