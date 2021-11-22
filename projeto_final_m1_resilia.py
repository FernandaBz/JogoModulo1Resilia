################################################ Apresetação ###########################################################
#Este jogo é uma saga pelo Reino de Misar onde 3 personagens lutam para achar as 6 chaves mágicas e libertar o Rei Zoltar.
#Eles não sabem no entanto, que o Rei não está preso entre grades e sim enfeitiçado. Ele foi transformado em um dragão
# de 3 cabeças e eles precisam destruir Macla para desfazer o feitiço.

#Separei cada movimento dos personagens com funções e condicionais que se repetem com certo padrão para manter a coerência
# de passos.
#Aqui estão variáveis básicas, serão acrescentadas outras no decorrer do jogo.

################################################ Variáveis #############################################################
personagem1 = ('Lilith')
personagem2 = ('Argo')
personagem3 = ('Alix')
escolha_jogador = ('Escolha o personagem: ')
sair_do_jogo1 = ('Ok. Saindo...')
fase_1_contexto = ('Lilith, Argo e Alix estavam passeando em Terras Distantes quando Misar foi dominada pelo exército de Macla. '
                         '\nVendo a destruição do reino os amigos criam um plano para libertar o Rei Zoltar que é mantido como escravo.\n')
fase_1_contexto_2 = ('Será preciso achar 6 chaves mágicas que estão guardadas com os 6 seres mais antigos do Reino. \n'
                     'Cada jovem seguirá por um caminho diferente recolhendo duas chaves cada um e se encontrarão no castelo \npara salvar Zoltar e o reino de Misar.')

#Contexto do jogo com a história que será contada.
############################################## Entrada do jogo #########################################################
print('+' * 50)


mensagem_inicial = input('Você está em Misar! Um reino mágico dominado por Macla, \numa feiticeira em busca de vingança.')
print(mensagem_inicial)

print('+' * 50)
contexto1 = input('Três jovens amigos tentarão libertar o Rei Zoltar \ne derrotar o exército de Macla para tornar Misar livre novamente.')
print(contexto1)

print('+' * 50)

#Função ainda com contexto do jogo.
#Coloquei essa função aqui pois preferi ter a opção de encaixá-la mais ao longo do jogo.
def escolha_personagens_2 ():
   print (input(fase_1_contexto))
   print('+' * 50)
   print (input(fase_1_contexto_2))
   print('+' * 50)

escolha_personagens_2()

######################################## Função apresentação personagens ###############################################
#Função com todos os personagens
def apresentacao_personagens ():
    print(f'\n{personagem1}: Princesa \nForça: Coragem \nHabilidade: Agilidade \nArma principal: Adaga')
    print('+' * 50)

    print(f'\n{personagem2}: Guerreiro \nForça: Inteligência \nHabilidade: Força física \nArma principal: Espada')
    print('+' * 50)

    print(f'\n{personagem3}: Feiticeira \nForça: Controle da mente \nHabilidade: Telecinese \nArma principal: Cajado')
    print('+' * 50)

#Função com apresentações Lilith
def apresentacao_personagens_lilith():
    print(f'\n{personagem1}: Princesa \nForça: Coragem \nHabilidade: Agilidade \nArma principal: Adaga')
    print('+' * 50)

#Função com apresentações Argo
def apresentacao_personagens_argo():
    print(f'\n{personagem2}: Guerreiro \nForça: Inteligência \nHabilidade: Força física \nArma principal: Espada')
    print('+' * 50)

#Função com apresentações Alix
def apresentacao_personagens_alix():
    print(f'\n{personagem3}: Feiticeira \nForça: Controle da mente \nHabilidade: Telecinese \nArma principal: Cajado')
    print('+' * 50)

############################################# Função LILITH fase FINAL #################################################
def lilith_batalha_final():
    print('DESCREVER BATALHA FINAL LILITH\n')
    print('[1] GANHA.')
    print('[2] ESCOLHE 2 MORRE.')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('VENCE')
            print(f'{personagem1} parece não acreditar. O Reino de Misar começa a tomar sua forma original. ')
            quit()

            condicao = False
        elif opcao.upper() == '2':
            print('MORREU.')
            print('GAME OVER')
            quit()

        # else:
        #     print('Opção inválida. Escolha um dos 2 CAMINHOS')


#Função castelo que chama outras funções -------
def lilith_final_castelo_1():
    print(f'Finalmente {personagem1} chega ao Castelo. O lugar que ela conhece como lar e que está tomado pelo exército de Macla.\n'
          f'Ela terá que se encontrar com {personagem2} e {personagem3} para que com as 6 chaves eles possam abrir a prisão encantada e\n'
          'libertar Zoltar.\n')
    print('+' * 50)
    print(f'{personagem1} encontra {personagem2} no estábulo. Argo felizmente {personagem2} conseguiur juntar\n'
                  f'as chaves vermelha e amarela. {personagem2} não pode seguir com a princesa agora, ele precisa agora\n'
                  f'cumprir uma missão dada pelo Ferreiro. {personagem1} parte então para encontrar {personagem3} no lugar\n'
                  f'que elas sempre brincavam.\n')
    print('+' * 50)
    print(f'{personagem1} encontra {personagem3} na cozinha. A jovem feiticeira foi orientada pelo Mago a fazer \n'
                  f'um feitiço usando no local para proteger seus pais. Ela entrega as chaves violeta e branca para\n'
                  f'{personagem1} que agora segue ao encontro de {personagem2} no estbábulo.\n')
    print('+' * 50)
    print(input('CLIQUE ENTER PARA SEGUIR!'))

    print(lilith_batalha_final())


#Função passa de fase e chama f castelo. Tb dá opção de sair do jogo.
def castelo_apresentacao_lilith ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!\n')
    print ('Seguir para a próxima fase CASTELO?')
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
            quit()
        else:
            print('Opção inválida. Escolha uma das opções ')


############################################# Funções LILITH fase DOIS ##################################################
#Função riacho que chama outras funções
def lilith_riacho_1():
    print('+' * 50)
    print(f'{personagem1} está na beira do riacho. Ela que pegar a chave encantada AZUL com Irlin.\n')
    print(f'{personagem1} ouviu dizer que Irlin é um ser muito bom e acredita que ela não terá problemas\n'
          'em entregar a chave AZUL. Mas para chegar até ela a princesa precisa mergulhar pelo único\n'
          'caminho possível: \n')

    print('[1] MERGULHAR NA PARTE MAIS ESCURA DO RIACHO.')
    print('[2] MERGULHAR NA PARTE MAIS FUNDA DO RIACHO.')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(f'{personagem1} escolheu a parte mais escura e ficou presa nos galhos aquáticos.\n'
                  'Ela não conseguirá encontrar Irlin no fundo do Riacho.')
            print('GAME OVER')
            quit()

            condicao = False
        elif opcao.upper() == '2':
            print(f'{personagem1} nada com toda sua força até encontrar Irlin no fundo do Riacho.\n'
                  'Irlin é realmente bondosa e lhe entrega a chave AZUL.')
            print ('+' * 50)
            print (castelo_apresentacao_lilith())

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

#Função passa de fase e chama f riacho. Tb dá opção de sair do jogo.
def riacho_apresentacao ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!\n')

    print ('Seguir para a próxima fase RIACHO?')
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
            quit()
        else:
            print('Opção inválida. Escolha uma das opções ')


############################################# Funções LILITH fase UM ####################################################
#Caso lilith não passe direto da fase floresta ela tem uma missão de ajuda a cumprir.
#Essa função finaliza o jogo ou chama f seguinte
def lilith_ajuda_1 ():
    print(f'{personagem1} precisa de usar uma erva para curar Jawbolt antes que ele morra.')
    print ('Qual dessas ela deve usar? ')
    print('[1] SEGUIR PARA DIREITA E ENCONTRAR A CENTELLA.')
    print('[2] SEGUIR PARA ESQUERDA E ENCONTRAR O TEIXO. ')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('lilith passa a Centella nos ferimentos de Jawbolt. Ele recobre a consciência \n'
                  'e está muito grato. Ele entrega chave VERDE para Lilith que pode continuar sua busca.')
            print('+' * 50)
            print (riacho_apresentacao())

            condicao = False
        elif opcao.upper() == "2":
            print('Infelizmente essa é a opção errada. E não dará tempo de pegar a outra erva.')
            print('Sem a ajuda dele ela nunca poderá encontrar a chave e seguir o plano.')
            print('GAME OVER')
            quit()

#Função floresta que chama outras funções
def lilith_floresta_1():
    print(f'\n{personagem1} está na floresta e percebe que as coisas estão diferentes. Chegando à pedra mágica um silêncio toma conta do lugar.\n'
          'De repente um estrondo. Passos fortes. Lilith se assusta, mas precisa enfrentar Jawbolt que está na sua frente, ele parece ferido e cansado.'
          f'\n{personagem1} está em cima da pedra mágica e percebe que sua adaga caiu no chão. Prestes a ser atacada\n''ela deve decidir:\n')
        # print(apresentacao_personagens_lilith())

    print('[1] CONTAR A JAWBOLT QUE ELA QUER SALVAR O REINO ANTES DE ATACÁ-LO ')
    print('[2] PEGAR A ADAGA MESMO ASSIM E USAR CONTRA JAWBOLT ')
    print('[3] SE DEFENDER COM SUA AGILIDADE E TENTAR PASSAR POR JAWBOLT ATÉ O GUARDIÃO DA CHAVE VERDE.')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('lILITH CONVENCE JAWBOLT A CURAR SEU FERIMENTO.')
            print('Ele reconhece a nobreza da jovem e lhe entrega a chave VERDE.\n')
            print(riacho_apresentacao())

            condicao = False
        elif opcao.upper() == "2":
            print('LILITH DECIDIU USAR A ADAGA E MATA JAWBOLT COM UM GOLPE NO CORAÇÃO.\n')
            print('Mas Lilith não sabia que Jawbolt era o real guardião da chave VERDE.\n')
            print('Sem a ajuda dele ela nunca poderá encontrar a chave e seguir o plano.\n')
            print('GAME OVER')
            quit()

        elif opcao.upper() == "3":
            print('LILITH CONSEGUE PASSAR POR JAWBOLT QUE FICOU CAÍDO. NA ENTRADA DO TEMPLO \n'
                  'ELA TENTA ENCONTRAR E GUARDIÃO E NÃO VÊ NINGUÉM\n')
            print('+' * 50)
            print('Jawbolt lhe conta que é ele o real guardião da chave VERDE.\n')
            print(f'{personagem1} decide ajudá-lo, mas ele perde a consciência e ela precisará de ajuda\n')
            print(lilith_ajuda_1 ())

        else:
            print('Opção inválida. Escolha uma das três ações.')

#Função com início 1 da personagem Lilith que chama f inicio 1
def lilith_inicio_1():
    print ('VOCÊ ESCOLHEU JOGAR COM LILITH')
    print (apresentacao_personagens_lilith())
    print(f'{personagem1} começará sua saga pela FLORESTA.')
    print('+' * 50)
    print (input(lilith_inicio_2()))

#Função com início 2 da personagem Lilith que chama f floresta
def lilith_inicio_2():
    print(f'{personagem1} conhece muito bem cada árvore ali, os animais que habitam e também os \n'
          'perigos que existem lá. Para chegar à chave encantada VERDE ela precisa convencer \n'
          'Jawbolt, o ogro guardião a deixá-la passar.')
    print(lilith_floresta_1())


############################################# Função ARGO fase FINAL #################################################
def argo_batalha_final():
    print('DESCREVER BATALHA FINAL LILITH\n')
    print('[1] ESCOLHE 1 VENCE.')
    print('[2] ESCOLHE 2 MORRE.')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('_____________ ')
            print('VENCE')
            quit()

            condicao = False
        elif opcao.upper() == '2':
            print('MORREU.')
            print('GAME OVER')
            quit()

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')


#Função riacho que chama outras funções
def argo_final_castelo_1():
    print(f'Argo chega ao castelo e segue para encontrar {personagem1} e sua irmã {personagem3}.')
    print('+' * 50)
    print(f'{personagem2} encontra {personagem1} no Salão entrando por uma passagem secreta que só os amigos conhecem.\n'
          f'Ele recebe as chaves azul e verde e vai encontrar sua irmã na cozinha do castelo.')
    print('+' * 50)
    print(f'{personagem2} encontra sua irmã {personagem3} na cozinha. Depois de um longo abraço, {personagem3} afirma que\n'
          f'deve ficar ali para salvar seus pais. Então Argo recolhe as chaves que estão com ela e segue para a batalha final.')

    print(input('CLIQUE ENTER PARA SEGUIR!'))
    print (argo_batalha_final())

#Função passa de fase e chama f castelo. Tb dá opção de sair do jogo.
def castelo_apresentacao_argo ():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para o Castelo?')
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
            quit()
        else:
            print('Opção inválida. Escolha uma das opções ')


############################################# Função ARGO fase DOIS ##################################################
#Função vila que chama outras funções
def argo_vila_1():
    print('Agora Argo chega a Vila dos Elfos. Ele sabe que terá que estar atento. Os elfos são antigos aliados do Rei Zoltar,\n'
          'mas que agora vivem sua vida independente. Argo profura por Olit o Elfo mais antigo da vila. Os elfos então\n'
          'decidem que se Argo acertar o caminho certo a seguir ele poderá falar com Olit:')

    print('[1] ALTO DA MONTANHA DOS ELFOS')
    print('[2] SEGUIR PELO VALE ENCANTADO')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('QUE PENA, ESCOLHA ERRADA.')
            print('GAME OVER')
            quit()

            condicao = False
        elif opcao.upper() == '2':
            print('Pelo caminho do vale encantado Argo chega a uma casa isolada, lá está Olit.\n'
                  'Ele lhe entrega a chave a Argo segue sua viagem.')
            print('O QUE ACONTECEU COM ARGO (VENCEU DESAFIO)')
            print(castelo_apresentacao_argo())


        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')
#Função passa de fase e chama f vila dos elfos. Tb dá opção de sair do jogo.
def vila_apresentacao ():
    print('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print('Seguir para Vila dos Elfos?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(argo_vila_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            quit()
        else:
            print('Opção inválida. Escolha uma das opções ')


############################################# Função ARGO fase UM ####################################################
#Função vila que chama outras funções
def argo_ferreiro_1():
    print('Argo encontra o Ferreiro no seu humilde casebre. O Ferreiro decide ajudá-lo, mas exige que Argo deixe ali sua espada\n'
          'e siga sua saga até o Castelo sem ela. Como Argo deve prosseguir?')
    print('[1] DAR SUA ESPADA EM TROCA DA CHAVE AMARELA')
    print('[2] TOMAR A CHAVE A FORÇA, JÁ QUE O FERREIRO É VELHO E NÃO PODE SE DEFENDER')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
                print('Mesmo cético das palavras do Ferreiro Argo decide pelo bem do Reino e deixa sua espada.\n'
                      'Argo recebe a chave amarela e a guarda com todo cuidado. Agora ele seguirá para a vila em busca da\n'
                      'chave vermelha.')
                print (vila_apresentacao())

        elif opcao.upper() == "2":
            print('Argo desconfia do Ferreiro e decide enfrentá-lo. Ele no entanto não esperava que o senhor fosse ainda tão forte.\n'
                  'Acontece que com um único golpe o Ferreiro dá um golpe e destrói a chave amarela. Argo não conseguirá cumprir sua missão.')
            print('GAME OVER')
            quit()

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

#Função com início 1 da personagem Alix que chama f inicio 1
def argo_fase_1 ():
    print('ARGO COMEÇARÁ SUA SAGA PELO FERREIRO.')
    print('+' * 50)

    print('Argo segue para a casa do ferreiro. Ele é um antigo guerreiro que defendeu por muito tempo o Reino de Misar.\n'
          'Depois da morte de sua esposa o Ferreiro decidiu se isolar e viver de forma humilde.\n')
    print(argo_ferreiro_1())

############################################# Função ALIX fase FINAL #################################################
def alix_batalha_final():
    print('DESCREVER BATALHA FINAL LILITH\n')
    print('[1] ESCOLHE 2 MORRE.')
    print('[2] ESCOLHE 1 VENCE.')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '2':
            print('_____________ ')
            print('VENCE')
            quit()

            condicao = False
        elif opcao.upper() == '1':
            print('MORREU.')
            print('GAME OVER')
            quit()

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

#Função passa de fase e chama f riacho. Tb dá opção de sair do jogo.
def castelo_apresentacao_alix():
    print('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(alix_final_castelo_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            quit()
        else:
            print('Opção inválida. Escolha uma das opções ')

#Função vila que chama outras funções
def alix_final_castelo_1():
    print('Alix precisa ')
    print('+' * 50)
    print(f'{personagem3} encontra {personagem1} no Salão entrando por uma passagem secreta que só os amigos conhecem.')
    print()
    print(f'{personagem3} encontra sua irmão {personagem2} no estábulo.')
    print('_____________ ')
    print('_____________ ')
    print(input('CLIQUE ENTER PARA SEGUIR!'))
    print (alix_batalha_final())



############################################# Função ALIX fase DOIS ##################################################
#Função passa de fase e chama f riacho. Tb dá opção de sair do jogo.
def apresentacao_caverna():
    print ('PARABÉNS! VOCÊ PASSOU DE FASE!')
    print ('Seguir para a próxima fase?')
    print('[1] SIM, CONTINUAR.')
    print('[2] NÃO, ENCERRAR AQUI.')

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print(alix_caverna_1())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            quit()
        else:
            print('Opção inválida. Escolha uma das opções ')
#Função vila que chama outras funções
def alix_caverna_1():
    print('ALIX FASE CAVERNA')
    print('[1] ESCOLHA_1 VENCE')
    print('[2] ESCOLHA_2 MORRE')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (VENCEU DESAFIO)')
            print(castelo_apresentacao_alix())

            condicao = False
        elif opcao.upper() == '2':
            print('OK. SAINDO...')
            quit()

        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

############################################# Função ALIX fase UM ####################################################
#Função vila que chama outras funções
def alix_mago_1():
    print(f'{personagem3} chega na casa do Mago e sente a presença de outra pessoa. ')
    print('[1] ESCOLHA_1 MORRE')
    print('[2] ESCOLHA_2 DESAFIO')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == '1':
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (PERDEU DESAFIO)')
            print('GAME OVER')
            quit()

            condicao = False
        elif opcao.upper() == "2":
            print('_____________ ')
            print('O QUE ACONTECEU COM ALIX (VENCEU O DESAFIO)')
            print(apresentacao_caverna())


        else:
            print('Opção inválida. Escolha um dos 2 CAMINHOS')

#Função com início 1 da personagem Alix que chama f inicio 1
def alix_fase_1 ():
    print('Alix comecará sua saga pelo Mago')
    print('+' * 50)
    print('O Mago é o grande mestre da magia do Reino de Misar. Alix ainda não consegue entender porque ele não\n'
          'conseguiu impedir a invasão de Macla.')
    print(alix_mago_1())

######################################## Função escolha personagens ####################################################
#Função com escolhas dos personagens ou saído do jogo
def escolha_personagens ():
   print('Escolha com quem deseja jogar: ')
   print('+' * 50)
   print('[1] Lilith')
   print('[2] Argo')
   print('[3] Alix')
   print('+' * 50)
   print('[S] PARA SAIR DO JOGO')
   print('+' * 50)

   condicao = True
   while condicao:
       opcao = input('Digite a opção:  \n')
       if opcao.upper() == '1':
           print('+' * 50)
           print(lilith_inicio_1 ())

           condicao = False
       elif opcao.upper() == '2':
           print('+' * 50)
           print(argo_fase_1())

       elif opcao.upper() == '3':
           print('+' * 50)
           print(alix_fase_1())

       elif opcao.upper() == 'S':
           print('Ok. Saindo do jogo...')
           quit()

       else:
           print('Opção inválida. Escolha um dos 3 personagens')

########################################## Função jogar sim ou não #####################################################
#Opção jogar ou não
def opcao_jogar():
    print('\nAjude Lilith, Argo e Alix a libertar o rei Zoltar do feitiço de Macla.\n')
    print('+' * 50)
    print('\nVamos jogar agora?')

    print('[J] JOGAR AGORA!')
    print('[S] SAIR E JOGAR DEPOIS.')
    print('+' * 50)

    condicao = True
    while condicao:
        opcao = input('Digite a opção:  \n')
        if opcao.upper() == "J":
            print('Você escolheu jogar agora!')
            print('+' * 50)
            print('Conheça os personagens: ')
            print('+' * 50)
            print (apresentacao_personagens())
            print('+' * 50)
            print(escolha_personagens ())
            condicao = False
        elif opcao.upper() == 'S':
            print('Ok. Saindo do jogo...')
            quit()

        else:
            print('Opção inválida. Escolha J para JOGAR ou S para SAIR agora mesmoooooo.')

opcao_jogar()