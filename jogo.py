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
    print("Vilarejo\n")

    print ()

def vulcao():
    #leva para o vulcao
    print("vulcao\n")

    def inimigo1():

        lifeE = 1
        attackE= 1
        defenseE = 3
        aliveE = True

        return lifeE, attackE, defenseE, aliveE
    
    def inimigo2():
        
        lifeE = 1
        attackE= 1
        defenseE = 3
        aliveE = True

        return lifeE, attackE, defenseE, aliveE
    
    def inimigo3():
        
        lifeE = 30
        attackE= 40
        defenseE = 3
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
                    print (life)
                    print (vida)
                    resultAttack = max(random.randint(1, atack) - random.randint(1, defenseE), 0)

                    lifeE = max(lifeE - resultAttack, 0)

                    print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                    if lifeE <= 0:

                        aliveE = False 
                        print ("Fim do combate\n")
                        cont = 0
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
                    lifeE, attackE, defenseE, aliveE = inimigo2()
                    
                    while alive == True and aliveE == True:
                        cont = cont + 1
                        print (life)
                        print (vida)
                        resultAttack = max(random.randint(1, atack) - random.randint(1, defenseE), 0)

                        lifeE = max(lifeE - resultAttack, 0)

                        print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")

                        if lifeE <= 0:

                            aliveE = False 
                            print ("Fim do combate\n")
                            cont = 0
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
                    
            while alive == True and aliveE == True:
                cont = cont + 1
                print (life)
                print (vida)
                resultAttack = max(random.randint(1, atack) - random.randint(1, defenseE), 0)
                lifeE = max(lifeE - resultAttack, 0)
                print("voce atacou e deu", resultAttack, "de dano\nResta", lifeE, "de vida do inimigo\n")
                
                if lifeE <= 0:
                    aliveE = False 
                    print ("Fim do combate\n")
                    cont = 0
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
        
        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over")
            dead = 0 

        if aliveG == True:
            LevelComplet = True
            pause = input("aperte enter para continuar")
            limparTELA()
            print("Com a vitória sobre N’zurak, você sente uma onda de poder invadir seu corpo.")
            print("O fragmento escondido do verdadeiro poder de Legondi foi absorvido por Abyssviolet.")
            print("Sua chama agora pulsa em azul profundo. A espada exige mais... mas está satisfeita, por ora.")
            pause = input("Hora de enfrentar Sephiroth. Aperte qualquer tecla para continuar...\n")

            limparTELA()
            batalha_final()
        elif dead == 1:
            pause = input("aperte qualquer tecla para continuar:\n")
            limparTELA()
            print("game over") 
            dead = 0


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
    life = 10
    atack = 10
    defense = 1
    start_point = "V"
    info_stats = f"Vida: {life}\nAtaque: {atack}\nDefesa: {defense}"
    return life, atack, defense, start_point, info_stats

#apaga restos de info do console antes de iniciar 
limparTELA()

#variaveis pre definidas para usu global
decisao_ini = ""
decisao_city = ""
esco_persona = ""
start_point = ""
life, atack, defense, start_point, info_Stats = 0, 0, 0, "", ""

print("bem vindo! escolha seu personagem: ")

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


#define a variavel para usar de parametro na hora de dar respawn do personagem
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
    print("Talvez o vilarejo tenha algo a oferecer... ou quem sabe o precipício esconda uma verdade.")
    pause = input("Aperte qualquer tecla para continuar...\n")
    limparTELA()
    print("1- Investigar a Fenda do Vulcão?\n2- Viajar em busca de poder para o precipico ou para o vilarejo destruido?\n3- ignorar tudo e enfrentar Sephiroth com o Poder atual")

else:
    print("Voce escolheu o Mago\n")
    print("1- Investigar ponto de origem \n2- Viajar em busca de poder \n3- enfrentar Boss final")


#impede o uso de digitar errado
while decisao_ini != "1" and decisao_ini != "2" and decisao_ini != "3":
    #mensagem de teste
    print("\no que voce vai fazer agora? ¯\_(ツ)_/¯\n")

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
            decisao_city = input("1- vilarejo\n2- precipicio\n:")
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