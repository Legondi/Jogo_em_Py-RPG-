import random
import os

life = 100
Dudu = 100
surrender = False
choice = [0, 1, 2]

print("MATAR O DUDU AGORA? - 0")
print("Vilarejo- 1")
print("Precipicio- 2")
choice[0] = int(input("escolha seu caminho: "))

if choice[0, 1, 2] == 0:

    while life > 0 and Dudu > 0 and surrender == False:

     atack = random.randint(1, 5)

     print(life)
    
     DuduA = random.randint(10, 20)
     print(DuduA)

     print("pedir para que desista! - 0")
     print("atacar com bola de fogo (1 a 5 de dano) - 1")
     print("fugir - 2")

     choice1 = int(input("escolha: "))
    

     if choice1 == 0: 
           
           os.system('cls' if os.name == 'nt' else 'clear')

           paz = random.randint(1, 100)
           if paz == 100:
              print ("DUDU - OK! ;)", paz)
              surrender = True
          
           else:
              life = life - DuduA   
              print("ha ha morra!")
              print("DUDU atacou e deu ", DuduA, " de dano") 
     elif choice1 == 1:
            print ("voce atacou DUDU e deu ", atack, " de dano")
            Dudu = Dudu - atack
            print ("na rodada do DUDU ele atacou e deu ", DuduA, " de dano")
            life = life - DuduA
     else:
         choice[0, 1, 2] = 1


elif choice[0, 1, 2] == 1:
    print ("voce esta no vilarejo")
else:
    print("voce esta no precipicio")
   
    
print ("Sua vida:", life, "DUDU:", Dudu, "teste: ")