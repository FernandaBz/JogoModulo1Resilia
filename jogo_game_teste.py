################################################ Variáveis #############################################################

personagem1 = ('Lilith')
personagem2 = ('Argo')
personagem3 = ('Alix')
escolha_jogador = ('Escolha o personagem: ')
sair_do_jogo1 = ('Ok. Saindo...')
fase_1_contexto = ('Lilith, Argo e Alix estavam passeando em Terras Distantes quando Misar foi dominada pelo exército de Macla. '
                         '\nVendo a destruição do reino os amigos criam um plano para libertar o Rei Zoltar que é mantido como escravo.\n')
fase_1_caminho_1 = ('Cada jovem seguirá por um caminho diferente com a esperança de que ao menos um consiga chegar até o castelo.')

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

############################################# Função LILITH fase UM ####################################################
def lilith_fase_1 ():
    print('Escolha por onde LILITH começará sua saga:')
    print('[1] Floresta')
    print('[2] Riacho')
    print('[3] Vila')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input("Digite a opção:  \n")
        if opcao.upper() == "1":
            print("\nAQUI APRESENTO CAMINHO FLORESTA==")
            print("AQUI CHAMO FUNÇÃO FLORESTA LILITH")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO LILITH.")

            condicao = False
        elif opcao.upper() == "2":
            print("\nAQUI APRESENTO CAMINHO RIACHO==")
            print("AQUI CHAMO FUNÇÃO RIACHO LILITH")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO LILITH.")

        elif opcao.upper() == "3":
            print("\nAQUI APRESENTO CAMINHO VILA==")
            print("AQUI CHAMO FUNÇÃO VILA LILITH")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO LILITH.")
        else:
            print('Opção inválida. Escolha um dos 3 CAMINHOS')

############################################# Função ARGO fase UM ####################################################
def argo_fase_1 ():
    print('Escolha por onde ARGO começará sua saga:')
    print('[1] Floresta')
    print('[2] Riacho')
    print('[3] Vila')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input("Digite a opção:  \n")
        if opcao.upper() == "1":
            print("\nAQUI APRESENTO CAMINHO FLORESTA==")
            print("AQUI CHAMO FUNÇÃO FLORESTA ARGO")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ARGO.")

            condicao = False
        elif opcao.upper() == "2":
            print("\nAQUI APRESENTO CAMINHO RIACHO==")
            print("AQUI CHAMO FUNÇÃO RIACHO ARGO")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ARGO.")

        elif opcao.upper() == "3":
            print("\nAQUI APRESENTO CAMINHO VILA==")
            print("AQUI CHAMO FUNÇÃO VILA ARGO")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ARGO.")
        else:
            print('Opção inválida. Escolha um dos 3 CAMINHOS')

############################################# Função ALIX fase UM ####################################################
def alix_fase_1 ():
    print('Escolha por onde ALIX começará sua saga:')
    print('[1] Floresta')
    print('[2] Riacho')
    print('[3] Vila')
    print('+' * 40)

    condicao = True
    while condicao:
        opcao = input("Digite a opção:  \n")
        if opcao.upper() == "1":
            print("\nAQUI APRESENTO CAMINHO FLORESTA==")
            print("AQUI CHAMO FUNÇÃO FLORESTA ALIX")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ALIX.")

            condicao = False
        elif opcao.upper() == "2":
            print("\nAQUI APRESENTO CAMINHO RIACHO==")
            print("AQUI CHAMO FUNÇÃO RIACHO ALIX")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ALIX.")

        elif opcao.upper() == "3":
            print("\nAQUI APRESENTO CAMINHO VILA==")
            print("AQUI CHAMO FUNÇÃO VILA ALIX")
            print("AQUI CHAMO A FUNÇÃO PARA ESCOLHER CAMINHO ALIX.")
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
       opcao = input("Digite a opção:  \n")
       if opcao.upper() == "1":
           print ('Você escolheu jogar com LILITH')
           print('+' * 40)
           print(fase_1_contexto)
           print(fase_1_caminho_1)
           print('+' * 40)
           print(lilith_fase_1 ())

           condicao = False
       elif opcao.upper() == "2":
           print('Você escolheu jogar com ARGO')
           print('+' * 40)
           print(fase_1_contexto)
           print(fase_1_caminho_1)
           print('+' * 40)
           print(argo_fase_1())

       elif opcao.upper() == "3":
           print('Você escolheu jogar com ALIX')
           print('+' * 40)
           print(fase_1_contexto)
           print(fase_1_caminho_1)
           print('+' * 40)
           print(alix_fase_1())

       elif opcao.upper() == "S":
           print("Ok. Saindo do jogo...")
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
        opcao = input("Digite a opção:  \n")
        if opcao.upper() == "J":
            print('Você escolheu jogar agora!')
            print('+' * 40)
            print("Conheça os personagens:")
            print(apresentacao_personagens())
            print('+' * 40)
            print(escolha_personagens ())
            condicao = False
        elif opcao.upper() == "S":
            print("Ok. Saindo do jogo...")
            break

        else:
            print("Opção inválida. Escolha J para JOGAR ou S para SAIR agora.")

opcao_jogar()