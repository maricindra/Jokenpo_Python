#Jokenpô com OR.
#usando a biblioteca random.
import random

# introdução ao usuario.
print("Bem vindo ao Jokenpô") 

# Armazenar as opções em uma lista.
opcoes=["pedra","papel","tesoura"]

# criando a entrada de dados para o usuário.
jogada_do_usuario = input("\n" "Escolha: Pedra, Papel ou Tesoura \n")

# criando a escolha do computador usando a lista opcoes.
jogada_do_computador= random.choice(opcoes)

# Direcionando o usuário com suas escolhas
print("\n" "Você escolheu",jogada_do_usuario)
# Informando a escolha do computador
print("O computador escolheu", jogada_do_computador)

#criando possibilidades de empates(leitura dos dados inseridos em Maiusculo OU Minusculo
if jogada_do_usuario.lower() == jogada_do_computador:
    print("\n""EMPATE!")
    
# Criando possibilidades de Vitória
elif (jogada_do_usuario.lower() == "pedra" and jogada_do_computador == "tesoura") or (jogada_do_usuario.lower() == "papel" and jogada_do_computador=="pedra") or (jogada_do_usuario.lower()== "tesoura" and jogada_do_computador == "papel"):
    print("\n""Você vencêu!!!")

# Criando possibilidades de derrota
elif (jogada_do_usuario.lower() == "tesoura" and jogada_do_computador == "pedra") or (jogada_do_usuario.lower() == "pedra" and jogada_do_computador=="papel") or (jogada_do_usuario.lower()== "papel" and jogada_do_computador == "tesoura"):
    print("\n""Você Perdeu!!!")

#Criando possibilidades de erro de digitação e guiando novamente o usuário ao inicio do codigo
else: 
    print("\n""Você digitou outra coisa....")
