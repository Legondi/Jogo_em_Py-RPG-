import random
import os



def limparTELA():
    #limpa o console quando requisitado para deixar o ambiente mais limpo
    os.system('cls' if os.name == 'nt' else 'clear')

def batalha_final():
    #leva para a batalha final do jogo
    print("batalha final")


    
    #Define os status do chefe final
    def sephiroth():
        lifeE = 400
        attackE= 50
        defenseE = 24
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    # Variáveis de controle
    cont = 0
    alive = True
    aliveG = True
    LevelComplet = False
    vida = life
    esco_lutar = ""
    dead = 0
    
    
    while aliveG == True and LevelComplet == False:
        while esco_lutar != "1" and esco_lutar != "2":
            print("Parabéns! Você chegou ao final da jornada.")
            print("Foi uma batalha longa e desafiadora...")
            print("Mas agora, finalmente, está diante do lendário SEPHIROTH.")
            print("Prepare-se para o confronto final!")
            esco_lutar = input("1- lutar\n2- fugir\n:")

            if esco_lutar == "1":
                limparTELA()
                print("voce escolheu lutar\n")
                lifeE, attackE, defenseE, aliveE = sephiroth()

                while alive == True and aliveE == True:
                    cont = cont + 1
                    resultAttack = max(random.randint(1, atack) - random.randint(1, defenseE), 0)

                    lifeE = max(lifeE - resultAttack, 0)

                    print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do sephiroth\n")

                    if lifeE <= 0:

                        aliveE = False 
                        print("╔════════════════════════════════════════════╗")
                        print("║         O FIM DO COMBATE CHEGOU!           ║")
                        print("║       Você superou todos os desafios!      ║")
                        print("║       A vitória é sua, grande herói!       ║")
                        print("╚════════════════════════════════════════════╝\n")
                        cont = 0
                        vida = life
                        #add levelComplet True para encerrar o while e finalizar o game (Leonardo)
                        LevelComplet = True
                        break

                    else:

                        pause = input("rodada do adversario aperte qualquer tecla para continuar:\n")
                        limparTELA()

                    resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)

                    vida = max(vida - resultAttackE, 0)

                    print("voce foi atacado e recebeu", resultAttackE, "de dano\nResta", vida, "da sua vida\n")
                    
                    if vida <= 0:

                        alive = False 
                        print("╔════════════════════════════════════════════╗")
                        print("║           O FIM DO COMBATE CHEGOU!         ║")
                        print("║      Você enfrentou tudo... e caiu!        ║")
                        print("║           Seu destino foi selado.          ║")
                        print("╚════════════════════════════════════════════╝\n")
                        cont = 0
                        aliveG = False
                        dead = dead + 1
                        break

                    else:

                        print ("Fim da rodada", cont,"\n")
                        pause = input("aperte qualquer tecla para continuar:\n")
                        limparTELA()
            elif esco_lutar == "2":
                limparTELA()
                aliveG = False
                print("╔════════════════════════════════════════════╗")
                print("║           VOCÊ DEU MEIA-VOLTA...           ║")
                print("║   Fugiu como um covarde diante do perigo.  ║")
                print("║     O mundo esperava um herói... mas       ║")
                print("║         recebeu um fujão patético.         ║")
                print("╚════════════════════════════════════════════╝\n")


            else:
                limparTELA()
                print("NAO EXISTE ESSA OPCAO!!!!!\n")

def vilarejo():
    #leva para o vilarejo
    print("Vilarejo\n")

    print ()

def vulcao():
    #leva para o vulcao
    global Qtdlutas, life, atack, defense, level, xpAtual   
    print("vulcao\n")

    def inimigo1():

        lifeE = 20
        attackE= 10
        defenseE = 40
        aliveE = True

        return lifeE, attackE, defenseE, aliveE

    def inimigo2():

        lifeE = 70
        attackE= 18
        defenseE = 15
        aliveE = True

        return lifeE, attackE, defenseE, aliveE

    def inimigo3():

        lifeE = 100
        attackE= 30
        defenseE = 12
        aliveE = True

        return lifeE, attackE, defenseE, aliveE

    cont = 0
    alive = True
    aliveG = True
    LevelComplet = False
    vida = life
    esco_lutar = ""
    dead = 0

    print("Você decidiu adentrar as Fendas de Fulgor, uma região oculta no interior do vulcão Legondira.")
    print("O calor ali queima até o próprio fogo. Legondi sussurra dentro da espada: ")
    print('“Quer o verdadeiro poder das Chamas? Vá até onde nem o inferno ousa queimar.”')
    pause = input("Aperte qualquer tecla para continuar...\n")


    print("Primeiro inimigo: Ashkar, o Guardião das Cinzas.")
    print("Um antigo guerreiro fracassado que tentou dominar Abyssviolet.")
    print("Lento, resistente, ataca com explosões de cinza quente.")
    pause = input("Prepare-se para lutar. Aperte qualquer tecla...\n")


    while aliveG == True and LevelComplet == False:
        while esco_lutar != "1" and esco_lutar != "2":
            esco_lutar = input("1- lutar\n2- fugir\n:")

            if esco_lutar == "1":
                limparTELA()
                print("voce escolheu lutar\n")
                lifeE, attackE, defenseE, aliveE = inimigo1()

                while alive == True and aliveE == True:
                    cont = cont + 1
                    Qtdlutas = Qtdlutas + 1
                    resultAttack = max(random.randint(1, int(atack + (lifeE / 6))) - random.randint(1, defenseE), 0)
                    lifeE = max(lifeE - resultAttack, 0)

                    print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                    if lifeE <= 0:

                        aliveE = False 
                        print ("Fim do combate\n")
                        vida = life
                        break

                    else:

                        pause = input("rodada do adversario aperte qualquer tecla para continuar:\n")
                        limparTELA()

                    resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)

                    vida = max(vida - resultAttackE, 0)

                    print("voce foi atacado e recebeu", resultAttackE, "de dano\nResta", vida, "da sua vida\n")

                    if vida <= 0:

                        alive = False 
                        print ("Fim do combate\n")
                        cont = 0
                        aliveG = False
                        dead = dead + 1
                        break

                    else:

                        print ("Fim da rodada", cont,"\n")
                        pause = input("aperte qualquer tecla para continuar:\n")
                        limparTELA()
            elif esco_lutar == "2":
                limparTELA()
                print("voce fugiu\n")


            else:
                limparTELA()
                print("NAO EXISTE ESSA OPCAO!!!!!\n")


            if esco_lutar == "1" and dead == 0:
                if aliveG == True and lifeE <= 0:
                    pause = input("aperte qualquer tecla para continuar:\n")
                    limparTELA()
                    print("Você derrotou Ashkar, o Guardião das Cinzas.")
                    print("Ele se desfaz em cinzas, revelando um fragmento de poder escondido.")
                    pause = input("Aperte qualquer tecla para continuar...\n")
                    
                    limparTELA()
                    if cont <= 6:
                        print("Você derrotou Ashkar com facilidade. Ele não era digno de ser seu oponente.")
                        sistema_de_xp()
                    elif cont <= 15:
                        print("Você derrotou Ashkar com dificuldade. Ele era um adversário formidável.")
                        sistema_de_xp()

        

        if aliveG == True:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()

            print("Segundo inimigo: Igraya, a Salamandra da Ira.")
            print("Um monstro ancestral de magma que persegue calor mágico.")
            print("Rápida, imprevisível, absorve calor para tentar apagar sua armadura viva.")
            pause = input("Aperte qualquer tecla para continuar...\n")

            esco_lutar = ""

            while esco_lutar != "1" and esco_lutar != "2":

                esco_lutar = input("1- lutar\n2- fugir\n:")

                if esco_lutar == "1":
                    limparTELA()
                    print("voce escolheu lutar\n")
                    cont = 0
                    lifeE, attackE, defenseE, aliveE = inimigo2()

                    while alive == True and aliveE == True:
                        cont = cont + 1
                        Qtdlutas = Qtdlutas + 1
                        resultAttack = max(random.randint(1, int(atack + (lifeE / 6))) - random.randint(1, defenseE), 0)
                        lifeE = max(lifeE - resultAttack, 0)

                        print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                        if lifeE <= 0:

                            aliveE = False 
                            print ("Fim do combate\n")
                            vida = life
                            break


                        else:

                            pause = input("rodada do adversario aperte qualquer tecla para continuar:\n")
                            limparTELA()

                        resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)

                        vida = max(vida - resultAttackE, 0)

                        print("voce foi atacado e recebeu", resultAttackE, "de dano\nResta", vida, "da sua vida\n")

                        if vida <= 0:

                            alive = False 
                            print ("Fim do combate\n")
                            cont = 0
                            aliveG = False
                            dead = 1
                            break

                        else:

                            print ("Fim da rodada", cont,"\n")
                            pause = input("aperte qualquer tecla para continuar:\n")
                            limparTELA()
                elif esco_lutar == "2":
                    limparTELA()
                    print("voce fugiu\n")

                else:
                    limparTELA()
                    print("...\n")

                if esco_lutar == "1" and dead == 0:
                    if aliveG == True and lifeE <= 0:
                        pause = input("aperte qualquer tecla para continuar:\n")
                        limparTELA()
                        print("Você derrotou Igraya, a Salamandra da Ira.")
                        print("Ao cair, seu corpo se cristaliza, deixando para trás um núcleo incandescente de poder.")
                        pause = input("Aperte qualquer tecla para continuar...\n")

                    limparTELA()
                    if cont <= 6:
                        print("Você derrotou Igraya com facilidade. Suas ilusões não foram páreo para sua determinação.")
                        sistema_de_xp()
                    elif cont <= 15:
                        print("Você derrotou Igraya com dificuldade. Suas ilusões quase o levaram à derrota.")
                        sistema_de_xp()

        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over")
            dead = 0

        if aliveG == True:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("Terceiro inimigo: N’zurak, o Portador do Fragmento.")
            print("Um reflexo distorcido de você mesma. Ele não luta por justiça. Luta por diversão.")
            print("Seu estilo muda a cada rodada. Ele copia e distorce suas próprias técnicas.")
            pause = input("Você está prestes a enfrentar o reflexo da sua alma. Aperte qualquer tecla...\n")

            lifeE, attackE, defenseE, aliveE = inimigo3()

            pause = input("voce esta indo para a batalha final obrigatoria da fenda do vulcao\nAperte qualquer tecla para continuar")
            limparTELA()

            cont = 0
            while alive == True and aliveE == True:
                
                cont = cont + 1
                Qtdlutas = Qtdlutas + 1

                resultAttack = max(random.randint(1, int(atack + (lifeE / 6))) - random.randint(1, defenseE), 0)
                lifeE = max(lifeE - resultAttack, 0)
                print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                if lifeE <= 0:
                    aliveE = False 
                    print ("Fim do combate\n")
                    vida = life
                    dead = 0
                    
                    if dead == 0:
                        
                        if aliveG == True and lifeE <= 0:
                            pause = input("aperte qualquer tecla para continuar:\n")
                            limparTELA()
                            print("Você derrotou N’zurak, o Portador do Fragmento.")
                            print("Ao cair, ele libera o último fragmento do poder flamejante que selava o coração do vulcão.")
                            pause = input("Aperte qualquer tecla para continuar...\n")

                        limparTELA()
                        if cont <= 6:
                            print("Você derrotou N’zurak com facilidade. Sua conexão com a magia ancestral o tornou imbatível.")
                            sistema_de_xp()
                        elif cont <= 15:
                            print("Você derrotou N’zurak com dificuldade. Sua magia quase o sobrepujou, mas sua determinação prevaleceu.")
                            sistema_de_xp()
                    break
                else:
                    pause = input("rodada do adversario aperte qualquer tecla para continuar:\n")
                    limparTELA()

                resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                vida = max(vida - resultAttackE, 0)
                print("voce foi atacado e recebeu", resultAttackE, "de dano\nResta", vida, "da sua vida\n")

                if vida <= 0:
                    alive = False 
                    print ("Fim do combate\n")
                    cont = 0
                    aliveG = False
                    dead = 1
                    break
                else:
                    print ("Fim da rodada", cont,"\n")
                    pause = input("aperte qualquer tecla para continuar:\n")
                    limparTELA()

                
        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over")
            dead = 0 

        if aliveG == True:
            LevelComplet = True
            pause = input("aperte enter para continuar")
            limparTELA()

            if Qtdlutas >= 2:
            
                print("Com a vitória sobre N’zurak, você sente uma onda de poder invadir seu corpo.")
                print("O fragmento escondido do verdadeiro poder de Legondi foi absorvido por Abyssviolet.")
                print("Sua chama agora pulsa em azul profundo. A espada exige mais... mas está satisfeita, por ora.")
                pause = input("Hora de enfrentar Sephiroth. Aperte qualquer tecla para continuar...\n")
                limparTELA()
            
                atack =+ 75
                life =+ 250
                defense =+ 40
                mostrar_status()
                pause = input("Pressione qualquer tecla para continuar...\n")
                print("Então você vai atrás do grande inimigo Sephiroth viajando a libertalia atras de acabar com a escuridão do mundo .")
                batalha_final()
                exit()

            elif Qtdlutas < 2: 
                print("Você está pronto o suficiente para enfrentar o verdadeiro desafio.")
                pause = input("Você sente o verdadeiro poder da magia ancestral. Pressione qualquer tecla para continuar...\n")
                limparTELA()
                print("E não ganha poder dos antigos magos elfos que habitavam as ruínas pois seu corpo não esta fortalecido o suficiente.")
                print("Agora terá que ir enfrentar o verdadeiro desafio sem esse poder.")
                pause = input("Pressione qualquer tecla para continuar...\n")
                limparTELA()

                mostrar_status()
                pause = input("Pressione qualquer tecla para continuar...\n")

                print("Então você vai atrás do grande inimigo Sephiroth viajando a libertalia atras de acabar com a escuridão do mundo mesmo sem receber o grande poder .")
                pause = input("Pressione qualquer tecla para continuar...\n")
                limparTELA()
                batalha_final()
                exit()

        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over") 
            dead = 0


def precipicio():
    #leva para o precipicio
    global Qtdlutas, life, atack, defense, level, xpAtual   
    print("O precipício da Morte\n")

    def inimigo1_pre():
        lifeE = 2
        attackE = 2
        defenseE = 2
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    def inimigo2_pre():
        lifeE = 3
        attackE = 3
        defenseE = 3
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    def inimigo3_pre():
        lifeE = 4
        attackE = 6
        defenseE = 5
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    cont = 0
    alive = True
    aliveG = True
    LevelComplet = False
    vida = life
    esco_lutar = ""
    dead = 0

    print("Você decide explorar o precipício da Morte, um local misterioso onde o silêncio pulsa com misterios amaldiçoados.")
    print("Os estalares das pedras vibram a sua volta. Ecos de antigos forasteitos ressoam pelas paredes.")
    pause = input("Aperte qualquer tecla para continuar...\n")

    print("Primeiro inimigo: Firelot, um homem de pedra.")
    print("Um ser feito de pura força e 300kg de pedra, forte, mas com uam agilidade lenta.")
    pause = input("Prepare-se para lutar. Aperte qualquer tecla...\n")

    while aliveG and not LevelComplet:
        while esco_lutar != "1" and esco_lutar != "2":
            esco_lutar = input("1- lutar\n2- fugir\n:")

            if esco_lutar == "1":
                limparTELA()
                print("Você escolheu lutar\n")
                lifeE, attackE, defenseE, aliveE = inimigo1_pre()

                while alive and aliveE:
                    cont += 1
                    Qtdlutas += 1
                    resultAttack = max(random.randint(2, atack + 2) - random.randint(1, defenseE), 0)
                    lifeE = max(lifeE - resultAttack, 0)

                    print("Você conjurou um ataque que causou", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                    if lifeE <= 0:
                        aliveE = False  
                        print("Fim do combate\n")
                        cont = 0
                        vida = life
                        break
                    else:
                        pause = input("Rodada do inimigo. Aperte qualquer tecla...\n")
                        limparTELA()

                    resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                    vida = max(vida - resultAttackE, 0)

                    print("Você foi atingido por um soco de pedra e sofreu", resultAttackE, "de dano\nSua vida atual:", vida)

                    if vida <= 0:
                        alive = False
                        print("Você foi derrotado.\n")
                        aliveG = False
                        dead = 1
                        break
                    else:
                        print("Fim da rodada", cont)
                        pause = input("Aperte qualquer tecla para continuar...\n")
                        limparTELA()

            elif esco_lutar == "2":
                limparTELA()
                print("Você fugiu da luta.\n")
                mostrar_status()
            else:
                limparTELA()
                print("Opção inválida!\n")


        if esco_lutar == "1":
            if aliveG == True and lifeE <= 0:
                pause = input("aperte qualquer tecla para continuar:\n")
                limparTELA()
                print("Você derrotou Firelot, o homem de pedra.")
                print("Ele se desfaz em pequenos pedregulhos, revelando um fragmento de poder escondido.")
                pause = input("Aperte qualquer tecla para continuar...\n")
                
                limparTELA()
                if cont <= 1:
                    print("Você derrotou Firelot com facilidade. Ele não era digno de ser seu oponente.")
                    sistema_de_xp()
                elif cont <= 3:
                    print("Você derrotou Firelot com dificuldade. Ele era um adversário formidável.")
                    sistema_de_xp()




        if aliveG:
            pause = input("Aperte qualquer tecla para continuar...\n")
            limparTELA()
            print("Segundo inimigo: Ninja, o fugitivo.")
            print("Uma Ninja que fugiu das cidades para viver uma vida misteriosa e perigosa.")
            pause = input("Prepare-se para enfrentar os ataques nas surdinas...\n")
            esco_lutar = ""

            while esco_lutar != "1" and esco_lutar != "2":
                esco_lutar = input("1- lutar\n2- fugir\n:")

                if esco_lutar == "1":
                    limparTELA()
                    print("Você escolheu lutar\n")
                    lifeE, attackE, defenseE, aliveE = inimigo2_pre()

                    while alive and aliveE:
                        cont += 1
                        Qtdlutas += 1
                        resultAttack = max(random.randint(2, atack + 2) - random.randint(1, defenseE), 0)
                        lifeE = max(lifeE - resultAttack, 0)

                        print("Você conjurou um ataque que causou", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                        if lifeE <= 0:
                            aliveE = False  
                            print("Fim do combate\n")
                            cont = 0
                            vida = life
                            break
                        else:
                            pause = input("Rodada do inimigo. Aperte qualquer tecla...\n")
                            limparTELA()

                        resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                        vida = max(vida - resultAttackE, 0)

                        print("Você foi atingido por uma shuriken envenenada e causou", resultAttackE, "de dano\nSua vida atual:", vida)

                        if vida <= 0:
                            alive = False
                            print("Você foi derrotado.\n")
                            aliveG = False
                            dead = 1
                            break
                        else:
                            print("Fim da rodada", cont)
                            pause = input("Aperte qualquer tecla para continuar...\n")
                            limparTELA()

                elif esco_lutar == "2":
                    limparTELA()
                    print("Você fugiu da luta.\n")
                    mostrar_status()
                else:
                    limparTELA()
                    print("Opção inválida!\n")

                if esco_lutar == "1":
                    if aliveG == True and lifeE <= 0:
                        pause = input("aperte qualquer tecla para continuar:\n")
                        limparTELA()
                        print("Você derrotou Ninja, o fugitivo.")
                        print("Ela desaparece em um redemoinho de ilusões, deixando para trás um fragmento de magia pura.")
                        pause = input("Aperte qualquer tecla para continuar...\n")
                    
                    limparTELA()
                    if cont <= 1:
                        print("Você derrotou Ninja com facilidade. Suas ilusões não foram páreo para sua determinação.")
                        sistema_de_xp()
                    elif cont <= 3:
                        print("Você derrotou Ninja com dificuldade. Suas ilusões quase o levaram à derrota.")
                        sistema_de_xp()

        if aliveG:
            pause = input("Aperte qualquer tecla para continuar...\n")
            limparTELA()
            print("Terceiro inimigo: Falconyon, o homem falcão.")
            print("Último guardião das ruínas, ele canaliza energia pura dos ventos  para atacar.")
            print("Essa será sua batalha mais difícil.")
            pause = input("Prepare-se para a batalha final!\n")
            esco_lutar = ""

            while esco_lutar != "1" and esco_lutar != "2":
                esco_lutar = input("1- lutar\n2- fugir\n:")

                if esco_lutar == "1":
                    limparTELA()
                    print("Você escolheu lutar\n")
                    lifeE, attackE, defenseE, aliveE = inimigo3_pre()

                    while alive and aliveE:
                        cont += 1
                        Qtdlutas += 1
                        resultAttack = max(random.randint(2, atack + 2) - random.randint(1, defenseE), 0)
                        lifeE = max(lifeE - resultAttack, 0)

                        print("Você conjurou um ataque que causou", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                        if lifeE <= 0:
                            aliveE = False  
                            print("Fim do combate\n")
                            cont = 0
                            vida = life
                            break
                        else:
                            pause = input("Rodada do inimigo. Aperte qualquer tecla...\n")
                            limparTELA()

                        resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                        vida = max(vida - resultAttackE, 0)

                        print("Você foi atingido por um ataque aéreo", resultAttackE, "de dano\nSua vida atual:", vida)

                        if vida <= 0:
                            alive = False
                            print("Você foi derrotado.\n")
                            aliveG = False
                            dead = 1
                            break
                        else:
                            print("Fim da rodada", cont)
                            pause = input("Aperte qualquer tecla para continuar...\n")
                            limparTELA()

                elif esco_lutar == "2":
                    limparTELA()
                    print("Você fugiu da luta.\n")
                    mostrar_status()
                else:
                    limparTELA()
                    print("Opção inválida!\n")
                
                if esco_lutar == "1":
                    if aliveG == True and lifeE <= 0:
                        pause = input("aperte qualquer tecla para continuar:\n")
                        limparTELA()
                        print("Você derrotou Falconyon, o homem falcão.")
                        print("Ele cai de asas no chão, sua energia se dissipando no ar, deixando para trás um núcleo de energia misterioso.")
                        pause = input("Aperte qualquer tecla para continuar...\n")
                    
                    limparTELA()
                    if cont <= 1:
                        print("Você derrotou Falconyon com facilidade. Sua conexão com a energia o tornou imbatível.")
                        sistema_de_xp()
                    elif cont <= 3:
                        print("Você derrotou Falconyon com dificuldade. Sua energia quase o sobrepujou, mas sua determinação prevaleceu.")
                        sistema_de_xp()
        if Qtdlutas >= 2:
            LevelComplet = True
            pause = input("Aperte qualquer tecla para continuar...\n")
            limparTELA()
            print("Com a vitória sobre Falconyon, sua mente se abre para segredos antigos.")
            print("Você domina a nova habilidade: 'Energia pedregulhosa'.")
            pause = input("Você sente o verdadeiro poder da energia ancestral. Pressione qualquer tecla para continuar...\n")
            print("Você se torna o novo Explorador misterioso do precipício Cozz.")
            print("A energia ancestral agora flui através de você, e o legado dos antigos dos que passaram por ai vive em seu coração.")
            print("Agora por sua coragem e determinação, você é digno de ser chamado de 'Explorador misterioso do precipício Cozz'.")
            pause = input("Você sente o verdadeiro poder da magia ancestral. Pressione qualquer tecla para continuar...\n")
            print("E ganha poder dos antigos exploradores que habitavam o precipício e seu corpo recebe tamanho poder.")
            print("Agora está pronto para enfrentar o verdadeiro desafio.")
            pause = input("Pressione qualquer tecla para continuar...\n")
            limparTELA()
            
            atack += 3000
            life += 15000
            defense += 5000
            mostrar_status()
            pause = input("Pressione qualquer tecla para continuar...\n")
            print("Então você vai atrás do grande inimigo Sephiroth viajando a libertalia atras de acabar com a escuridão do mundo .")
            batalha_final()
            exit()  

        elif Qtdlutas < 2: 
            print("Você está pronto o suficiente para enfrentar o verdadeiro desafio.")
            pause = input("Você sente o verdadeiro poder da magia ancestral. Pressione qualquer tecla para continuar...\n")
            limparTELA()
            print("E não ganha poder dos antigos magos elfos que habitavam as ruínas pois seu corpo não esta fortalecido o suficiente.")
            print("Agora terá que ir enfrentar o verdadeiro desafio sem esse poder.")
            pause = input("Pressione qualquer tecla para continuar...\n")
            limparTELA()
            
            mostrar_status()
            pause = input("Pressione qualquer tecla para continuar...\n")
            
            print("Então você vai atrás do grande inimigo Sephiroth viajando a libertalia atras de acabar com a escuridão do mundo mesmo sem receber o grande poder .")
            pause = input("Pressione qualquer tecla para continuar...\n")
            limparTELA()
            batalha_final()
            exit()

        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over") 
            dead = 0
    print("precipicio")

def floresta():
    # leva para as Ruínas Arcanas
    global Qtdlutas, life, atack, defense, level, xpAtual   
    print("As Ruínas Arcanas\n")

    def inimigo1_mago():
        lifeE = 2
        attackE = 2
        defenseE = 2
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    def inimigo2_mago():
        lifeE = 3
        attackE = 3
        defenseE = 3
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    def inimigo3_mago():
        lifeE = 4
        attackE = 6
        defenseE = 5
        aliveE = True
        return lifeE, attackE, defenseE, aliveE

    cont = 0
    alive = True
    aliveG = True
    LevelComplet = False
    vida = life
    esco_lutar = ""
    dead = 0

    print("Você decide explorar as Ruínas Arcanas, um local ancestral onde o éter pulsa com magia esquecida.")
    print("A varinha vibra em sua mão. Ecos de antigos magos ressoam pelas paredes.")
    pause = input("Aperte qualquer tecla para continuar...\n")

    print("Primeiro inimigo: Spectrus, o Fragmento de Luz.")
    print("Um ser feito de pura energia mágica, frágil, mas com ataques letais de luz concentrada.")
    pause = input("Prepare-se para lutar. Aperte qualquer tecla...\n")

    while aliveG and not LevelComplet:
        while esco_lutar != "1" and esco_lutar != "2":
            esco_lutar = input("1- lutar\n2- fugir\n:")

            if esco_lutar == "1":
                limparTELA()
                print("Você escolheu lutar\n")
                lifeE, attackE, defenseE, aliveE = inimigo1_mago()

                while alive and aliveE:
                    cont += 1
                    Qtdlutas += 1
                    resultAttack = max(random.randint(1, atack + int((0.2 * cont))) - random.randint(1, defenseE), 0)
                    lifeE = max(lifeE - resultAttack, 0)

                    print("Você conjurou uma magia que causou", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                    if lifeE <= 0:
                        aliveE = False  
                        print("Fim do combate\n")
                        cont = 0
                        vida = life
                        break
                    else:
                        pause = input("Rodada do inimigo. Aperte qualquer tecla...\n")
                        limparTELA()

                    resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                    vida = max(vida - resultAttackE, 0)

                    print("Você foi atingido por magia e sofreu", resultAttackE, "de dano\nSua vida atual:", vida)

                    if vida <= 0:
                        alive = False
                        print("Você foi derrotado.\n")
                        aliveG = False
                        dead = 1
                        break
                    else:
                        print("Fim da rodada", cont)
                        pause = input("Aperte qualquer tecla para continuar...\n")
                        limparTELA()

            elif esco_lutar == "2":
                limparTELA()
                print("Você fugiu da luta.\n")
                mostrar_status()
            else:
                limparTELA()
                print("Opção inválida!\n")


        if esco_lutar == "1":
            if aliveG == True and lifeE <= 0:
                pause = input("aperte qualquer tecla para continuar:\n")
                limparTELA()
                print("Você derrotou Ashkar, o Guardião das Cinzas.")
                print("Ele se desfaz em cinzas, revelando um fragmento de poder escondido.")
                pause = input("Aperte qualquer tecla para continuar...\n")
                
                limparTELA()
                if cont <= 1:
                    print("Você derrotou Ashkar com facilidade. Ele não era digno de ser seu oponente.")
                    sistema_de_xp()
                elif cont <= 3:
                    print("Você derrotou Ashkar com dificuldade. Ele era um adversário formidável.")
                    sistema_de_xp()


        if aliveG:
            pause = input("Aperte qualquer tecla para continuar...\n")
            limparTELA()
            print("Segundo inimigo: Igraya, a Tecelã do Caos.")
            print("Uma maga espectral que usa ilusões para confundir sua mente.")
            pause = input("Prepare-se para enfrentar as distorções arcanas...\n")
            esco_lutar = ""

            while esco_lutar != "1" and esco_lutar != "2":
                esco_lutar = input("1- lutar\n2- fugir\n:")

                if esco_lutar == "1":
                    limparTELA()
                    print("Você escolheu lutar\n")
                    lifeE, attackE, defenseE, aliveE = inimigo2_mago()

                    while alive and aliveE:
                        cont += 1
                        Qtdlutas += 1
                        resultAttack = max(random.randint(1, atack + int((0.2 * cont))) - random.randint(1, defenseE), 0)
                        lifeE = max(lifeE - resultAttack, 0)

                        print("Você conjurou uma magia que causou", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                        if lifeE <= 0:
                            aliveE = False  
                            print("Fim do combate\n")
                            cont = 0
                            vida = life
                            break
                        else:
                            pause = input("Rodada do inimigo. Aperte qualquer tecla...\n")
                            limparTELA()

                        resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                        vida = max(vida - resultAttackE, 0)

                        print("Você foi atingido por magia e sofreu", resultAttackE, "de dano\nSua vida atual:", vida)

                        if vida <= 0:

                            alive = False
                            print("Você foi derrotado.\n")
                            aliveG = False
                            dead = 1
                            break

                        else:
                            print("Fim da rodada", cont)
                            pause = input("Aperte qualquer tecla para continuar...\n")
                            limparTELA()

                elif esco_lutar == "2":
                    limparTELA()
                    print("Você fugiu da luta.\n")
                    mostrar_status()
                else:
                    limparTELA()
                    print("Opção inválida!\n")

        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over")
            dead = 0


        if esco_lutar == "1":
            if aliveG == True and lifeE <= 0:
                pause = input("aperte qualquer tecla para continuar:\n")
                limparTELA()
                print("Você derrotou Igraya, a Tecelã do Caos.")
                print("Ela desaparece em um redemoinho de ilusões, deixando para trás um fragmento de magia pura.")
                pause = input("Aperte qualquer tecla para continuar...\n")
            
            limparTELA()
            if cont <= 1:
                print("Você derrotou Igraya com facilidade. Suas ilusões não foram páreo para sua determinação.")
                sistema_de_xp()
            elif cont <= 3:
                print("Você derrotou Igraya com dificuldade. Suas ilusões quase o levaram à derrota.")
                sistema_de_xp()

        if aliveG:
            pause = input("Aperte qualquer tecla para continuar...\n")
            limparTELA()
            print("Terceiro inimigo: Vyserion, o Arcanista Sombrio.")
            print("Último guardião das ruínas, ele canaliza magia pura da terra para se regenerar.")
            print("Essa será sua batalha mais difícil.")
            pause = input("Prepare-se para a batalha final!\n")
        
            lifeE, attackE, defenseE, aliveE = inimigo3_mago()

            pause = input("voce esta indo para a batalha final obrigatoria da fenda do vulcao\nAperte qualquer tecla para continuar")
            limparTELA()
    
            while alive and aliveE:
                cont += 1
                Qtdlutas += 1

                resultAttack = max(random.randint(1, atack + int((0.2 * cont))) - random.randint(1, defenseE), 0)
                lifeE = max(lifeE - resultAttack, 0)
                print("Você conjurou uma magia que causou", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                if lifeE <= 0:
                    aliveE = False  
                    print("Fim do combate\n")
                    cont = 0
                    vida = life
                    break
                else:
                    pause = input("Rodada do inimigo. Aperte qualquer tecla...\n")
                    limparTELA()

                resultAttackE = max(random.randint(1, attackE) - random.randint(1, defense), 0)
                vida = max(vida - resultAttackE, 0)
                print("Você foi atingido por magia e sofreu", resultAttackE, "de dano\nSua vida atual:", vida)

                if vida <= 0:
                    alive = False
                    print("Você foi derrotado.\n")
                    aliveG = False
                    dead = 1
                    break
                else:
                    print("Fim da rodada", cont)
                    pause = input("Aperte qualquer tecla para continuar...\n")
                    limparTELA()
         
        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over")
            dead = 0 

                
        if esco_lutar == "1":
            mostrar_status()
            if aliveG == True and lifeE <= 0:
                pause = input("aperte qualquer tecla para continuar:\n")
                limparTELA()
                print("Você derrotou Vyserion, o Arcanista Sombrio.")
                print("Ele cai de joelhos, sua magia se dissipando no ar, deixando para trás um núcleo de energia arcana.")
                pause = input("Aperte qualquer tecla para continuar...\n")
            
            limparTELA()
            if cont <= 1:
                print("Você derrotou Vyserion com facilidade. Sua conexão com a magia ancestral o tornou imbatível.")
                sistema_de_xp()
            elif cont <= 3:
                print("Você derrotou Vyserion com dificuldade. Sua magia quase o sobrepujou, mas sua determinação prevaleceu.")
                sistema_de_xp()

        if Qtdlutas >= 2:
            LevelComplet = True
            pause = input("Aperte qualquer tecla para continuar...\n")
            limparTELA()
            print("Com a vitória sobre Vyserion, sua mente se abre para segredos antigos.")
            print("Você domina um novo feitiço ✨🌀🔮: 'Éter Primordial'.")
            pause = input("Você sente o verdadeiro poder da magia ancestral. Pressione qualquer tecla para continuar...\n")
            print("Você se torna o novo guardião das Ruínas Arcanas.")
            print("A magia ancestral agora flui através de você, e o legado dos antigos magos vive em seu coração.")
            print("Agora por sua coragem e determinação, você é digno de ser chamado de 'Guardião das Ruínas Arcanas'.")
            pause = input("Você sente o verdadeiro poder da magia ancestral. Pressione qualquer tecla para continuar...\n")
            print("E ganha poder dos antigos magos elfos que habitavam as ruínas e seu corpo recebe tamanho poder.")
            print("Agora está pronto para enfrentar o verdadeiro desafio.")
            pause = input("Pressione qualquer tecla para continuar...\n")
            limparTELA()
            
            atack =+ 3000
            life =+ 15000
            defense =+ 5000
            mostrar_status()
            pause = input("Pressione qualquer tecla para continuar...\n")
            print("Então você vai atrás do grande inimigo Sephiroth viajando a libertalia atras de acabar com a escuridão do mundo .")
            batalha_final()
            exit()  

        elif Qtdlutas < 2: 
            print("Você está pronto o suficiente para enfrentar o verdadeiro desafio.")
            pause = input("Você sente o verdadeiro poder da magia ancestral. Pressione qualquer tecla para continuar...\n")
            limparTELA()
            print("E não ganha poder dos antigos magos elfos que habitavam as ruínas pois seu corpo não esta fortalecido o suficiente.")
            print("Agora terá que ir enfrentar o verdadeiro desafio sem esse poder.")
            pause = input("Pressione qualquer tecla para continuar...\n")
            limparTELA()
            
            mostrar_status()
            pause = input("Pressione qualquer tecla para continuar...\n")
            
            print("Então você vai atrás do grande inimigo Sephiroth viajando a libertalia atras de acabar com a escuridão do mundo mesmo sem receber o grande poder .")
            pause = input("Pressione qualquer tecla para continuar...\n")
            limparTELA()
            batalha_final()
            exit()

        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over") 
            dead = 0


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
    life = 100
    atack = 40
    defense = 15
    start_point = "V"
    info_stats = f"Vida: {life}\nAtaque: {atack}\nDefesa: {defense}"
    return life, atack, defense, start_point, info_stats


def upar_personagem():
 
 global life, atack, defense
 escolha = 0
 while escolha != "1" and escolha != "2" and escolha != "3": 
    print("\nVocê subiu de nível! Escolha um atributo para aumentar:")
    print("1 - Aumentar Vida")
    print("2 - Aumentar Ataque")
    print("3 - Aumentar Defesa")
    escolha = input("Digite o número da opção: ")

    if  escolha != "1" and escolha != "2" and escolha != "3":
        print("Opção inválida. Tente novamente.")
        continue

    if escolha == "1":
        life += 5
        print("✨ Vida aumentada!")
    elif escolha == "2":
        atack += 5
        print("⚔️ Ataque aumentado!")
    elif escolha == "3":
        defense += 5
        print("🛡️ Defesa aumentada!")
    else:
        print("Escolha inválida. Nenhum atributo foi aumentado.")

    if  escolha != "1" and escolha != "2" and escolha != "3":
        print("Opção inválida. Tente novamente.")
        pause = input("Aperte qualquer tecla para continuar...\n")
        limparTELA()

def xpProximoNivel():
    #calcula o xp para o proximo nivel
    return 100 + (level - 1) * 50

def calcular_xp_ganho(cont):
    xpbase = 100
    penalidade = (cont - 1) * 10
    return max(20, xpbase - penalidade)

def mostrar_status():
    print(f"\n📊 Status Atual:")
    print(f"Nível: {level}")
    print(f"XP: {xpAtual}/{xpProximoNivel()}")
    print(f"Vida: {life}, Ataque: {atack}, Defesa: {defense}")

def xp_ganho():
    #calcula o xp ganho
    xpAtual += calcular_xp_ganho()
    print(f"Você ganhou {xpAtual} de XP!")
    if xpAtual >= xpProximoNivel():
        level += 1
        upar_personagem()
        xpAtual = 0
        print(f"Parabéns! Você subiu para o nível {level}!")

def ganhar_xp(xp_ganho):
    global xpAtual, level
    # ganha xp e verifica se o level up
    xpAtual += xp_ganho
    while xpAtual >= xpProximoNivel():
        xpAtual -= xpProximoNivel()
        level += 1
        print(f"\n🔼 Subiu para o Nível {level}!")
        upar_personagem()

def sistema_de_xp():
    #Função que executa o sistema de XP baseado nas rodadas da batalha.
    global cont
    xp_ganho = calcular_xp_ganho(cont)
    print(f"\n✨ XP ganho: {xp_ganho}")
    ganhar_xp(xp_ganho)
    pause = input("Aperte qualquer tecla para continuar...\n")
    mostrar_status()
#apaga restos de info do console antes de iniciar 
limparTELA()

#variaveis pre definidas para usu global
decisao_ini = ""
decisao_city = ""
esco_persona = ""
start_point = ""
life, atack, defense, start_point, info_Stats = 0, 0, 0, "", ""

xpbase , xpAtual  = 0, 1
level = 1
cont = 0
Qtdlutas = 0   



print("╔════════════════════════════════════════════════════════════════════════════════════╗")
print("║                                                                                    ║")
print("║                                | L | I | B | E | R | T | A |                       ║")
print("║                                                                                    ║")
print("║                          UMA JORNADA DE MAGIA, BRAVURA E REDENÇÃO                   ║")
print("║                                                                                    ║")
print("║        Em um reino mergulhado nas trevas, os últimos heróis se levantam.            ║")
print("║     Magos e guerreiros se unem para desafiar o mal que consome Libertália.          ║")
print("║      Suas escolhas forjarão o destino do reino... e do seu próprio legado.          ║")
print("║                                                                                    ║")
print("║                          ★ LIBERTA — O DESTINO ESTÁ EM SUAS MÃOS ★                  ║")
print("║                                                                                    ║")
print("╚════════════════════════════════════════════════════════════════════════════════════╝\n")

pause = input("Pressione ENTER para iniciar sua aventura...\n")

print("O Reino de Libertália era um símbolo de equilíbrio e poder, onde magos e guerreiros viviam em paz,")
print("protegendo suas terras sob a liderança justa do Império Libertália — uma cidade majestosa localizada no centro do reino.\n")

print("Porém, essa paz foi quebrada quando Sephiroth, um ser sombrio de imenso poder, surgiu do desconhecido")
print("e iniciou um ataque devastador. Ele destruiu o Vilarejo de Ludwig, corrompeu antigos protetores,")
print("e tomou a cidade imperial, mergulhando-a em trevas.\n")

print("Agora, os últimos heróis se erguem: magos da Floresta Encantada de Nack e guerreiros do Vulcão Legondi")
print("embarcam em uma jornada para enfrentar os lacaios de Sephiroth e libertar o coração do reino.\n")

print("O Vulcão Legondi é uma terra de provações. Forjado em calor e cinzas, ele molda os guerreiros mais resistentes —")
print("forjados não apenas em batalha, mas na dor, no sacrifício e na honra ancestral.")
print("Dizem que as Fendas de Fulgor, escondidas dentro de Legondi, sussurram o nome dos que têm destino grandioso.")
print("Quem ousa encarar suas profundezas, raramente retorna o mesmo.\n")

print("Enquanto isso, a Floresta de Nack pulsa com magia selvagem.")
print("Suas árvores milenares guardam segredos e espíritos antigos que concedem poder aos magos dignos.\n")

print("O Canyon Cozz, ao oeste, é um deserto de pedra e vento, onde um ninja sombrio guarda artefatos esquecidos.")
print("E ao norte, os escombros do Vilarejo de Ludwig ecoam os gritos dos caídos, sob o domínio de um guardião corrompido.\n")

print("Você é um dos últimos escolhidos. A jornada começa agora.\n")

input("Pressione ENTER para escolher o seu personagem \n")


#validação de escolha
while esco_persona != "1" and esco_persona != "2":
    esco_persona = input("1- Mago\n2- Guerreira\n3- Informações de Personagens:")

    #estrutura para decidir o personagem (previne erros)
    if esco_persona == "1":
        limparTELA()
        #carrega status do mago
        life, atack, defense, start_point, info_Stats = mage()
    elif esco_persona == "2":
        limparTELA()
        #carrega status da guerreira
        life, atack, defense, start_point, info_Stats = valkyrie()
    elif esco_persona == "3":
        limparTELA()

        #estrura para ver as informacoes e decidir qual personagem o uso tem mais familiaridade
        esco_info = ""

        #estrutura para decidir qual o status do personagem quer ver (previne erros)
        while esco_info != "1" and esco_info != "2" and esco_info != "3":
            print("qual dos persongens voce quer ver historia e status:?")
            esco_info = input("1- Mago\n2- Guerreira\n3- voltar\n:")
            limparTELA()

            if esco_info == "1":
                life, atack, defense, start_point, info_Stats = mage() 

                #printa as infos com base na escolha
                print(info_Stats)
                #pausa o codigo para a visualização das infos
                Exit = input("\naperte qualquer tecla para sair:")

            elif esco_info == "2":
                life, atack, defense, start_point, info_Stats = valkyrie() 

                #printa as infos com base na escolha
                print(info_Stats)
                #pausa o codigo para a visualização das infos
                Exit = input("\naperte qualquer tecla para sair:")

            elif esco_info == "3":
                #volta para o primeiro menu e limpa o console para uma melhor visu
                limparTELA()
            else:
                #impede o erro
                limparTELA()
                print("opcao invalida\n") 

        limparTELA()
    else:
        #impede o erro
        limparTELA()
        print("persongam nao encontrado ;(\n")

#passado a historia e contexto para o usu surge as opcoes!


#                                    A
#PONTO DE BAIXA ALTERAÇÃO DE CODIGO  |


#_____________________________________________________________________________________________________________________________________


#PONTO DE ALTA ALTERAÇÃO DE CODIGO  |
#                                  V


#define a variavel para usar de parametro na hora de dar respawn
if start_point == "V":

    print("Quando Sephiroth, o ser sombrio de poder devastador, lançou à distância sua maldição sobre Legondira — um feitiço de aniquilação total — ninguém conseguiu reagir. Exceto ela.")
    print("No momento em que tudo parecia perdido, Neriah se lançou entre a magia e os inocentes, e ergueu uma arma proibida: a espada lendária Abyssviolet.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()
    print("A lenda dizia que qualquer um que empunhasse a espada seria destruído por ela, ou consumido pela alma do antigo guerreiro Legondi, selado em seu núcleo.")
    print("Mas, ao vê-la, o espírito guerreiro ancestral não viu uma escolhida. Viu entretenimento.")
    print('“Você vai me dar batalhas. Vitórias. Gritos e caos. Você vai me entreter.”')
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("A energia das trevas lançada por Sephiroth foi absorvida pela lâmina.")
    print("Ao invés de matá-la, fundiu-se ao seu corpo. As Chamas de Abyssviolet surgiram em um tom roxo profundo azulado, criando uma armadura viva ao redor de Neriah — feita de puro fogo, que nunca a queima.")
    print("Ela resistiu não por pureza. Mas porque Legondi se divertiu.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("Desde então, a fronteira entre bravura e soberba se desfaz em cada passo da guerreira.")
    print("Ela é reverenciada como uma enviada do próprio fogo — temida, seguida, adorada.")
    print("A cidade está de pé, mas ferida. Os sobreviventes a olham com temor e fé.")
    print("Ela sabe que o inimigo não está longe, mas que não o enfrentará como está. A espada exige mais. Mais poder. Mais conflito.")
    pause = input("Aperte qualquer tecla para continuar...\n")

    limparTELA()

    print("A voz de Legondi ecoa em sua mente, abafando até o som do mundo ao redor:")
    print('“As Fendas de Fulgor te chamarão de volta... mas será que você é digna do fogo que arde lá dentro?”')
    print("Você sente o poder queimando sob seus pés — mas sabe que há outros caminhos. Por enquanto.")
    print("Talvez o Vilarejo de Ludwig ainda esconda vestígios do passado... ou ecos de algo que se recusa a morrer.")
    print("Talvez o Canyon Cozz revele os segredos enterrados na areia... ou a sombra de quem ainda vigia das rochas.")   
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()
    print("1- Investigar a Fenda do Vulcão?\n2- Viajar em busca de poder para o Canyon Cozz ou para o Vilarejo de Ludwig?\n3- ignorar tudo e enfrentar Sephiroth com o Poder atual")

else:
    print("Quando Sephiroth, o ser sombrio de poder devastador, lançou sua maldição sobre Legondira — uma onda de morte e esquecimento — ninguém conseguiu reagir. Exceto ele.")
    print("Nas profundezas da Floresta Encantada de Nack, onde os sussurros das árvores guardam a memória do mundo, Arthur Leywin despertou de um transe antigo.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("As copas estremeciam sem vento. O canto dos pássaros cessou. Os rios que serpenteavam os carvalhos ancestrais pareciam hesitar.")
    print("Os elfos anciões, guardiões do Equilíbrio Mágico, sabiam: algo havia tocado o coração do mundo.")
    print("Arthur Leywin, criado entre pergaminhos vivos e espíritos antigos, foi o escolhido pelo Círculo Verde para compreender essa ruptura.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()


    print("Guiado por visões, ele encontrou o Altar das Folhas Eternas — um santuário escondido na raiz da árvore mais velha da floresta.")
    print("Lá, diante do espelho de Thal’Miren, artefato selado por eras, Arthur Leywin viu a destruição de Legondira. O céu rasgado. O fogo eterno. Sephiroth.")
    print("E, no reflexo, viu a si mesmo... em chamas, em sombra, em ascensão.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("Ao tocar o espelho, Arthur Leywin foi marcado pela Essência Espectral — uma magia viva, mutável, que desafia as leis do tempo e da matéria.")
    print("Ele não apenas viu o futuro: ele se tornou parte dele.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("Agora, a floresta o teme e o reverencia. Os animais se ajoelham, os rios murmuram seu nome, e os espíritos antigos o testam.")
    print("Mas o tempo urge. Sephiroth não está longe — sua presença já fere o mundo. O Imperador de Libertalia começa a silenciar magos. E as sombras se alastram.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("A voz do espelho ecoa em sua mente como folhas ao vento:")
    print('“Os olhos do inimigo já pousaram sobre ti... mas és tu quem escolhe onde cairá tua primeira chama.”')
    print("Você sente a floresta chamando... mas sabe que o mundo além das árvores precisa de você.")
    print("O vilarejo de Ludwig foi destruído, mas pode conter relíquias dos primeiros elfos humanos.")
    print("O Cânion Cozz esconde ruínas onde a magia flui sem regras. E o Império Libertalia... talvez nem tudo esteja perdido por lá.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()

    print("1- Permanecer na Floresta de Nack e desvendar os ecos da magia élfica?")
    print("2- Viajar até o Vilarejo destruído de Ludwig ou explorar o Cânion Cozz em busca de relíquias antigas?")
    print("3- Arriscar tudo e seguir até Libertalia ou mesmo enfrentar Sephiroth antes que ele ataque novamente?")



#impede o uso de digitar errado
while decisao_ini != "1" and decisao_ini != "2" and decisao_ini != "3":
    #mensagem de teste

    #estrutura para decidir inicio da historia

    decisao_ini = input("\n:")

    # separa os caminhos para acessar a funcao de cada mapa em especifico
    if decisao_ini == "1":
        limparTELA()
        if start_point == "V":
            vulcao()
        else:
            floresta()
    elif decisao_ini == "2":
        limparTELA()
        while decisao_city != "1" and decisao_city != "2":
            print("escolha seu destino:")
            decisao_city = input("1-Vilarejo destruído de Ludwig\n2- Cânion Cozz  \n:")
            if decisao_city == "1":
                limparTELA()
                vilarejo()
            elif decisao_city == "2":
                limparTELA()
                precipicio()
            else:
                limparTELA()
                print("Deixa de ser teimoso e escolhe 1 ou 2!!!\n")

    elif decisao_ini == "3":
        limparTELA()
        batalha_final()
    else:
        limparTELA()
        print("vamos la eu sei que voce consegue, escolha 1, 2 ou 3 ;)")
        limparTELA()
        print("1- Permanecer na Floresta de Nack e desvendar os ecos da magia élfica?")
        print("2- Viajar até o Vilarejo destruído de Ludwig ou explorar o Cânion Cozz em busca de relíquias antigas?")
        print("3- Arriscar tudo e seguir até Libertalia ou mesmo enfrentar Sephiroth antes que ele ataque novamente?")
        print("\no que voce vai fazer agora eu sei que voçê não é tão burro ¯\_(ツ)_/¯\n")