#Jokenpô com OR
import random

print("Bem vindo ao Jokenpô")
opcoes=["pedra","papel","tesoura"]

jogada_do_usuario = input("\n" "Escolha: Pedra, Papel ou Tesoura \n")
jogada_do_computador= random.choice(opcoes)

print("\n" "Você escolheu",jogada_do_usuario)
print("O computador escolheu", jogada_do_computador)

#criando possibilidades de empates
if jogada_do_usuario.lower() == jogada_do_computador:
    print("\n""EMPATE!")

elif (jogada_do_usuario.lower() == "pedra" and jogada_do_computador == "tesoura") or (jogada_do_usuario.lower() == "papel" and jogada_do_computador=="pedra") or (jogada_do_usuario.lower()== "tesoura" and jogada_do_computador == "papel"):
    print("\n""Você vencêu!!!")

elif (jogada_do_usuario.lower() == "tesoura" and jogada_do_computador == "pedra") or (jogada_do_usuario.lower() == "pedra" and jogada_do_computador=="papel") or (jogada_do_usuario.lower()== "papel" and jogada_do_computador == "tesoura"):
    print("\n""Você Perdeu!!!")

else: 
    print("\n""Você digitou outra coisa....")
