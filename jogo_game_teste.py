################################################ Variáveis #############################################################

personagem1 = ('Lilith')
personagem2 = ('Argo')
personagem3 = ('Alix')
escolha_jogador = ('Escolha o personagem: ')
sair_do_jogo1 = ('Ok. Saindo...')
fase_1_contexto = ('Lilith, Argo e Alix estavam passeando em Terras Distantes quando Misar foi dominada pelo exército de Macla. '
                         '\nVendo a destruição do reino os amigos criam um plano para libertar o Rei Zoltar que é mantido como escravo.\n')
fase_1_contexto_2 = ('Será preciso achar 6 chaves mágicas que estão guardadas com os 6 seres mais antigos do Reino.')
fase_1_contexto_3 = ('Cada jovem seguirá por um caminho diferente recolhendo duas chaves cada um e se encontrarão no castelo para salvar Zoltar e o reino de Misar.')

############################################## Entrada do jogo #########################################################
print('+' * 40)

mensagem_inicial = input('Você está em Misar! Um reino mágico dominado por Macla, \numa feiticeira em busca de vingança.')
print(mensagem_inicial)

print('+' * 40)
contexto1 = input('Três jovens amigos tentarão libertar o Rei Zoltar \ne derrotar o exército de Macla para tornar Misar livre novamente.')
print(contexto1)

print('+' * 40)

######################################## Função apresentação personagens ###############################################
def apresentacao_personagens ():
    print ('\nLilith: Princesa \nForça: Coragem \nHabilidade: Agilidade \nArma principal: Adaga')
    print('+' * 40)

    print('\nArgo: Guerreiro \nForça: Inteligência \nHabilidade: Força física \nArma principal: Espada')
    print('+' * 40)

    print('\nAlix: Feiticeira \nForça: Controle da mente \nHabilidade: Telecinese \nArma principal: Cajado')
    print('+' * 40)

def apresentacao_personagens_lilith():
    print('\nLilith: Princesa \nForça: Coragem \nHabilidade: Agilidade \nArma principal: Adaga')
    print('+' * 40)

def apresentacao_personagens_argo():
    print('\nArgo: Guerreiro \nForça: Inteligência \nHabilidade: Força física \nArma principal: Espada')
    print('+' * 40)

def apresentacao_personagens_alix():
    print('\nAlix: Feiticeira \nForça: Controle da mente \nHabilidade: Telecinese \nArma principal: Cajado')
    print('+' * 40)

############################################# Função LILITH fase FINAL #################################################

def lilith_final_castelo_1():
    print('Finalmente Lilith chega ao Castelo. O lugar que ela conhece como lar e que está tomado pelo exército de Macla.\n'
          'Ela terá que se encontrar com Argo e Alix para que com as 6 chaves eles possam abrir a prisão encantada e\n '
          'libertar Zoltar.' '\nPor onde Lilith deve entrar no Castelo?')
    print('[1] PELO ESTÁBULO.')
    print('[2] PELA COZINHA.')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('_____________ ')
            print('LILITH ENCONTRA ARGO NO ESTÁBULO.')
            print('=CHAMAR CHAMAR FASE ESTÁBULO.=')

            condicao = False
        elif opcao.upper() == '2':
            print('Lilith encontra Alix na cozinha. Ela foi orientada pelo Mago a fazer um feitiço usando .....')
            print('=CHAMAR FASE COZINHA=')

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

def castelo_apresentacao_lilith ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(lilith_final_castelo_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            break
        else:
            print('Opção inválida. Escolha uma das opções ')


############################################# Funções LILITH fase DOIS ##################################################
def lilith_riacho_1():
    print ('RIACHO')
    print('+' * 40)
    print('Lilith está na beira do riacho. Ela que pegar a chave encantada AZUL com Irlin.\n')
    print('Lilith ouviu dizer que Irlin é um ser muito bom e acredita que ela não terá problemas\n'
          'em entregar a chave AZUL. Mas para chegar até ela a princesa precisa mergulhar pelo único\n'
          'caminho possível:')

    print('[1] MERGULHAR NA PARTE MAIS ESCURA DO RIACHO.')
    print('[2] MERGULHAR NA PARTE MAIS FUNDA DO RIACHO.')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('Lilith escolheu a parte mais escura e ficou presa nos galhos aquáticos.'
                  'Ela não conseguirá encontrar Irlin no fundo do Riacho.')
            print('GAME OVER')
            break

            condicao = False
        elif opcao.upper() == '2':
            print('Lilith nada com toda sua força até encontrar Irlin no fundo do Riacho.'
                  'Irlin é realmente bondosa e lhe entrega a chave AZUL.')
            print (floresta_apresentacao())

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

def riacho_apresentacao ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(lilith_riacho_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            break
        else:
            print('Opção inválida. Escolha uma das opções ')


############################################# Funções LILITH fase UM ####################################################

def lilith_ajuda_1 ():
    print('Lilith precisa de usar uma erva para curar Jawbolt antes que ele morra.')
    print ('Qual dessas ela deve usar? ')
    print('[1] SEGUIR PARA DIREITA E ENCONTRAR A CENTELLA.')
    print('[2] SEGUIR PARA ESQUERDA E ENCONTRAR O TEIXO. ')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('lilith passa a Centella nos ferimentos de Jawbolt. Ele recobre a consciência \n'
                  'e está muito grato. Ele entrega chave VERDE para Lilith que pode continuar sua busca.')
            print('+' * 40)

            condicao = False
        elif opcao.upper() == "2":
            print('Infelizmente essa é a opção errada. E não dará tempo de pegar a outra erva.')
            print('Sem a ajuda dele ela nunca poderá encontrar a chave e seguir o plano.')
            print('GAME OVER')
            break

def floresta_apresentacao ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(lilith_floresta_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            break
        else:
            print('Opção inválida. Escolha uma das opções ')


def lilith_floresta_1():
    print('FLORESTA')

    print('\nLilith está na floresta e percebe que as coisas estão diferentes. Chegando à pedra mágica um silêncio toma conta do lugar.\n'
          'De repente um estrondo. Passos fortes. Lilith se assusta, mas precisa enfrentar Jawbolt que está na sua frente, ele parece ferido e cansado.'
          '\nLilith está em cima da pedra mágica e percebe que sua adaga caiu no chão. Prestes a ser atacada\n''ela deve decidir:')
        # print(apresentacao_personagens_lilith())

    print('[1] CONTAR A JAWBOLT QUE ELA QUER SALVAR O REINO ANTES DE ATACÁ-LO ')
    print('[2] PEGAR A ADAGA MESMO ASSIM E USAR CONTRA JAWBOLT ')
    print('[3] SE DEFENDER COM SUA AGILIDADE E TENTAR PASSAR POR JAWBOLT ATÉ O GUARDIÃO DA CHAVE VERDE.')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('lILITH CONVENCE JAWBOLT A CURAR SEU FERIMENTO.\n')
            print ('Ele reconhece a nobreza da jovem e lhe entrega a chave VERDE.\n')

            condicao = False
        elif opcao.upper() == "2":
            print('LILITH DECIDIU USAR A ADAGA E MATA JAWBOLT COM UM GOLPE NO CORAÇÃO.\n')
            print('Mas Lilith não sabia que Jawbolt era o real guardião da chave VERDE.\n')
            print('Sem a ajuda dele ela nunca poderá encontrar a chave e seguir o plano.\n')
            print('GAME OVER')
            break

        elif opcao.upper() == "3":
            print('LILITH CONSEGUE PASSAR POR JAWBOLT QUE FICOU CAÍDO. NA ENTRADA DO TEMPLO \n'
                  'ELA TENTA ENCONTRAR E GUARDIÃO E NÃO VÊ NINGUÉM\n')
            print('+' * 40)
            print('Jawbolt lhe conta que é ele o real guardião da chave VERDE.\n')
            print('Lilith decide ajudá-lo, mas ele perde a consciência e ela precisará de ajuda\n')
            print(lilith_ajuda_1 ())

        else:
            print('Opção inválida. Escolha uma das três ações.')



def lilith_fase_1 ():
    print('Escolha por onde LILITH começará sua saga:')
    print('[1] FLORESTA - CHAVE VERDE')
    print('[2] FLORESTA - CHAVE AZUL')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('Lilith agora está na floresta. Ela conhece muito bem cada árvore ali, \n'
                  'os animais que habitam e também os perigos que existem lá. Para chegar \n'
                  'à chave encantada VERDE ela precisa convencer Jawbolt, o ogro guardião a deixá-la \n'
                  'passar.')
            print(lilith_floresta_1())

            print (riacho_apresentacao ())

            print(castelo_apresentacao_lilith())

            condicao = False
        elif opcao.upper() == "2":
            print('Lilith está na beira do riacho. Ela terá que nadar até o fundo e negociar \n'
                  'com Irlin, a guardiã das águas. Ela está com a chave encantada AZUL.')
            print(lilith_riacho_1())

            print (floresta_apresentacao())

            print (castelo_apresentacao_lilith())

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

############################################# Função ARGO fase FINAL #################################################
def argo_final_castelo_1():
    print('HISTÓRIA FASE UM E ESCOLHA DO QUE FAZER')
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (VENCEU O JOGO)')

            condicao = False
        elif opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (PERDEU O DESAFIO)')
            print('GAME OVER')
            break

        else:
            print('VER O QUE FAZER AQUI')

def castelo_apresentacao_argo ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(argo_final_castelo_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            break
        else:
            print('Opção inválida. Escolha uma das opções ')



############################################# Função ARGO fase DOIS ##################################################
def argo_vila_1():
    print('HISTÓRIA FASE UM E ESCOLHA DO QUE FAZER')
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (VENCEU DESAFIO)')
            print('CHAMAR FASE FINAL ARGO')

            condicao = False
        elif opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (PERDEU O DESAFIO)')
            print('GAME OVER')
            break

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

def vila_apresentacao ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(argo_final_castelo_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            break
        else:
            print('Opção inválida. Escolha uma das opções ')



############################################# Função ARGO fase UM ####################################################
def argo_ferreiro_1():
    print('HISTÓRIA NA FASE FERREIRO')
    print(funcao)
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('[3] ESCOLHA_3')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (VENCEU DESAFIO)')
            print('CHAMAR FASE DOIS ARGO')

            condicao = False
        elif opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (VENCEU DESAFIO)')
            print('CHAMAR FASE DOIS ARGO')

        elif opcao.upper() == "3":
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (PERDEU O DESAFIO)')
            print('GAME OVER')
            break

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')


############################################# Função ARGO fase DOIS ##################################################


def argo_fase_1 ():
    print('Escolha por onde ARGO começará sua saga:')
    print('[1] FERREIRO')
    print('[2] VILA DOS ELFOS')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('\nAQUI APRESENTO CAMINHO FERREIRO==')
            print(argo_floresta_1())
            print('AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ARGO.')

            condicao = False
        elif opcao.upper() == '2':
            print('\nAQUI APRESENTO CAMINHO VILA DOS ELFOS==')
            print(argo_riacho_1())
            print('AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ARGO.')

        else:
            print('Opção inválida. Escolha um dos CAMINHOS')

############################################# Função ALIX fase FINAL #################################################
def alix_final_castelo_1():
    print('HISTÓRIA FASE UM E ESCOLHA DO QUE FAZER')
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (VENCEU O JOGO)')

            condicao = False
        elif opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (PERDEU O DESAFIO)')
            print('GAME OVER')
            break

        else:
            print('VER O QUE FAZER AQUI')


############################################# Função ALIX fase TRES ##################################################
def alix_vila_1():
    print('HISTÓRIA FASE UM E ESCOLHA DO QUE FAZER')
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ARGO (VENCEU DESAFIO)')
            print('CHAMAR FASE FINAL ALIX')

            condicao = False
        elif opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (PERDEU O DESAFIO)')
            print('GAME OVER')
            break

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')


############################################# Função ALIX fase DOIS ##################################################
def alix_riacho_1():
    print('HISTÓRIA FASE UM E ESCOLHA DO QUE FAZER')
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (VENCEU DESAFIO)')
            print('CHAMAR FASE TRÊS ALIX')

            condicao = False
        elif opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (PERDEU O DESAFIO)')
            print('GAME OVER')
            break

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

############################################# Função ALIX fase UM ####################################################
def alix_floresta_1():
    print('HISTÓRIA FASE UM E ESCOLHA DO QUE FAZER')
    print(funcao)
    print('[1] ESCOLHA_1')
    print('[2] ESCOLHA_2')
    print('[3] ESCOLHA_3')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (PERDEU DESAFIO)')
            print('GAME OVER')
            break

            condicao = False
        elif opcao.upper() == '2':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (VENCEU O DESAFIO)')
            print('CHAMAR FASE DOIS ALIX')

        elif opcao.upper() == "3":
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (VENCEU O DESAFIO)')
            print('CHAMAR FASE DOIS ALIX')


        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')


def alix_fase_1 ():
    print('Escolha por onde ALIX começará sua saga:')
    print('[1] Floresta')
    print('[2] Riacho')
    print('[3] Vila')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('\nAQUI APRESENTO CAMINHO FLORESTA==')
            print(alix_floresta_1())
            print('AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ALIX.')

            condicao = False
        elif opcao.upper() == '2':
            print('\nAQUI APRESENTO CAMINHO RIACHO==')
            print(alix_riacho_1())
            print('AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ALIX.')

        elif opcao.upper() == '3':
            print('\nAQUI APRESENTO CAMINHO VILA==')
            print(alix_vila_1())
            print('AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ALIX.')
        else:
            print('Opção inválida. Escolha um dos 3 CAMINHOS')

######################################## Função escolha personagens ####################################################
def escolha_personagens ():
   print('Escolha com quem quer jogar: ')
   print('[1] Lilith')
   print('[2] Argo')
   print('[3] Alix')
   print('[S] PARA SAIR DO JOGO')
   print('+' * 40)

   condicao = True
   while condicao:
       opcao = input('Digite a opção:  \n')
       if opcao.upper() == '1':
           print ('Você escolheu jogar com LILITH')
           print('+' * 40)
           print(fase_1_contexto)
           print(fase_1_contexto_2)
           print(fase_1_contexto_3)
           print('+' * 40)
           print(lilith_fase_1 ())

           condicao = False
       elif opcao.upper() == '2':
           print('Você escolheu jogar com ARGO')
           print('+' * 40)
           print(fase_1_contexto)
           print(fase_1_contexto_2)
           print(fase_1_contexto_3)
           print('+' * 40)
           print(argo_fase_1())

       elif opcao.upper() == '3':
           print('Você escolheu jogar com ALIX')
           print('+' * 40)
           print(fase_1_contexto)
           print (fase_1_contexto_2)
           print(fase_1_contexto_3)
           print('+' * 40)
           print(alix_fase_1())

       elif opcao.upper() == 'S':
           print('Ok. Saindo do jogo...')
           break

       else:
           print('Opção inválida. Escolha um dos 3 personagens')

########################################## Função jogar sim ou não #####################################################
def opcao_jogar():
    print('\nAjude Lilith, Argo e Alix a libertar o rei Zoltar do feitiço de Macla.\n')
    print('+' * 40)
    print('\nVamos jogar agora?')

    print('[J] JOGAR AGORA!')
    print('[S] SAIR E JOGAR DEPOIS.')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == "J":
            print('Você escolheu jogar agora!')
            print('+' * 40)
            print('Conheça os personagens: ')
            print(apresentacao_personagens())
            print('+' * 40)
            print(escolha_personagens ())
            condicao = False
        elif opcao.upper() == 'S':
            print('Ok. Saindo do jogo...')
            break

        else:
            print('Opção inválida. Escolha J para JOGAR ou S para SAIR agora mesmoooooo.')

opcao_jogar()