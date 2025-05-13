import random
import os

def limparTELA():
      #limpa o console quando requisitado para deixar o ambiente mais limpo
      os.system('cls' if os.name == 'nt' else 'clear')

def batalha_final():
    #leva para a batalha final do jogo
    print("batalha final")

def vilarejo():
    #leva para o vilarejo
    print("Vilarejo")

def vulcao():
    #leva para o vulcao
    print("vulcao")

def precipicio():
    #leva para o precipicio
    print("precipicio")

def floresta():
    #leva para a floresta
    print("floresta")

def mage():
    #status do mago
    life = 10
    atack = 5
    defense = 6
    start_point = "F"
    info_stats = f"Vida: {life}\nAtaque: {atack}\nDefesa: {defense}"
    return life, atack, defense, start_point, info_stats

def valkyrie():
    #status da guerreira
    life = 12
    atack = 6
    defense = 2
    start_point = "V"
    info_stats = f"Vida: {life}\nAtaque: {atack}\nDefesa: {defense}"
    return life, atack, defense, start_point, info_stats

limparTELA()

esco_persona = ""
life, atack, defense, start_Point, info_Stats = 0, 0, 0, "", ""

print("bem vindo! escolha seu personagem: ")

while esco_persona != "1" and esco_persona != "2":

 esco_persona = input("1- Mago\n2- Guerreira\n3- Informações de Personagens:")

 if esco_persona == "1":
    limparTELA()
    life, atack, defense, start_Point, info_Stats = mage()
 elif esco_persona == "2":
    limparTELA()
    life, atack, defense, start_Point, info_Stats = valkyrie()
 elif esco_persona == "3":
    limparTELA()
    esco_info = ""
    while esco_info != "1" and esco_info != "2" and esco_info != "3":
        print("qual dos persongens voce quer ver historia e status:?")
        esco_info = input("1- Mago\n2- Guerreira\n3- voltar\n:")
        limparTELA()
    
        if esco_info == "1":
            life, atack, defense, start_Point, info_Stats = mage() 
            print(info_Stats)
            Exit = input("\naperte qualquer tecla para sair:")
        elif esco_info == "2":
            life, atack, defense, start_Point, info_Stats = valkyrie() 
            print(info_Stats)
            Exit = input("\naperte qualquer tecla para sair:")
        elif esco_info == "3":
            limparTELA()
        else:
           limparTELA()
           print("opcao invalida\n") 

    limparTELA()
 else:
    limparTELA()
    print("persongam nao encontrado ;(\n")

#passado a historia e contexto para o usu surge as opcoes!

if start_Point == "V":
    print("Voce escolheu a Guerreira\n")
else:
    print("Voce escolheu o Mago\n")

print("o que voce vai fazer agora? ¯\_(ツ)_/¯")
print()

decisao_ini = input("1- Buscar \n2- Guerreira\n3- Informações de Personagens:")

