from os import system
from time import sleep
def limpa(): return system('cls')


#Função para iniciar o jogo
def verificar_vencedor(player, contra):
    global tiro_atual
    limpa()
    print('Vez do Player ',  player)
    sleep(2)
    limpa()
    while True:
        #Executa a função de mostrar mapa com return padrão True, caso player erre um tiro, return se torna False
        while mostrar_mapa_jogo(player, contra):
            #Verifica se o Player é o vencedor pela contagem de tiros acertados
            if acertos[player] == 15:
                limpa()
                mostrar_mapa_jogo(player,contra)
                #Caso exista um vencedor, função verificar_vencedor() retorna True, satisfazendo o IF inicial
                return  True
            try:
                print('\nLegenda\n\033[46m\033[30m▦ \033[0;0m - Início ou fim de um barco\n\033[46m\033[30m▣ \033[0;0m - Corpo do barco\n\033[46m\033[31m✖ \033[0;0m - Tiro errado\n\033[46m  \033[0;0m - Água')
                if acerto:
                    print('\nJogue Novamente')
                tiro_atual = int(input('\n\nDigite uma coordenada (Ex: 3,0): ').replace(',',''))
                #Verifica se o tiro_atual não é igual aos anteriores que estão salvos numa lista
                if tiro_atual in tiros[player]:
                    #Caso sim, tiro_atual recebe None para não haver conflito ao executar a função de mostra_mapa_jogo()
                    tiro_atual = None
                    raise ValueError
                #Caso não, adiciona o valor do tiro dentro de uma lista
                tiros[player].append(tiro_atual)
            except:
                print("Posição já usada ou valor inválido")
        #Para a repetição quando o Player erra um tiro
        break
    mostrar_mapa_jogo(player, contra)
    sleep(3)
    return False


#Mostra mapa do jogo, verifica acertos/erros
def mostrar_mapa_jogo(player, contra):
    #Variáves que são necessárias para exibição do mapa
    global acertos, tiros, navios, tiro_atual, acerto
    limpa()
    #Tiro recebe inicialmente false para satisfazer a execução do while na linha 13
    tiro =  False
    #Exibe coordenadas do eixo x
    print('   0  1  2  3  4  5  6  7  8  9')
    #Contagem de Acertos do Player
    acertos[player] = 0
    #Formação do mapa
    for bloco in range(100):
        #Exibe coordenadas do eixo y
        if bloco in range(0, 100, 10):
            print(int(bloco/10), end='  ')
        #Executa caso o bloco esteja na lista de tiros do Player
        if bloco in tiros[player]:
            for navio, blocos in navios[contra].items():
                #Inicia caso os tiros estiverem no barco do Player Inimigo. Existe 3 caracteres para exibir: Acerto Inicio/Fim do barco, Acerto Corpo do Barco, Erro
                if bloco in blocos:
                    #Incrementa na variável de acertos
                    acertos[player] += 1
                    #Caso os tiros estejam na ultima posição do eixo x, vão pular uma linha
                    if bloco in range(9, 100, 10):
                        if bloco == blocos[-1] or bloco == blocos[0]:
                            #Acerto Inicio/Fim do barco
                            print('\033[46m\033[30m▦ \033[0;0m')
                        else:
                            #Acerto Corpo do Barco
                            print('\033[46m\033[30m▣ \033[0;0m')
                    #Caso os tiros estejam em qualquer posição do eixo x, exceto a ultima, vão manter-se na mesma linha
                    else:
                        if bloco == blocos[-1] or bloco == blocos[0]:
                            #Acerto Inicio/Fim do barco
                            print('\033[46m\033[30m▦', end='  ')
                        else:
                            #Acerto Corpo do Barco
                            print('\033[46m\033[30m▣', end='  ')
                    #Verifica se o Acerto é o ultimo tiro dado
                    if bloco == tiro_atual:
                        #Função retorna True
                        tiro = True
                        acerto =  True
                    break
                #Caso Erro
                elif navio == '2x1':
                    if bloco in range(9, 100, 10):
                        #Erro
                        print('\033[46m\033[31m✖ \033[0;0m')
                    else:
                        print('\033[46m\033[31m✖', end='  ')
                    #Verifica se o Erro é o ultimo tiro dado
                    if bloco == tiro_atual:
                        #Função retorna False
                        tiro =  True
                        acerto = False
                    break
        #Caso não houver tiro no bloco atual, exibirá a Água
        elif bloco in range(9, 100, 10):
            #Água 
            print('\033[46m  \033[0;0m')
        else:
            print('\033[46m ', end='  ')
    #Se houve um tiro na rodada. Função só se torna verdadeira após o primeiro tiro do jogo
    if tiro:
        return acerto
    return True        


#Mostrar mapa para colocar návios dos players. Quase a mesma lógica da função mostrar_mapa_jogo()
def mostrar_mapa_navios(player):
    print('    0  1  2  3  4  5  6  7  8  9')
    for bloco in range(100):
        #Váriavel para saber se o Player colocou algum návio no bloco. Caso sim, exibe o Barco. Caso não, exibe a Água
        navioP = False
        if bloco in range(0, 100, 10):
            print(int(bloco/10), end='  ')
        for  blocos in navios2[player].values():
            if bloco in blocos:
                if bloco in range(9, 100, 10):
                    if bloco == blocos[-1] or bloco == blocos[0]:
                        print('\033[46m\033[30m▣ \033[0;0m')
                    else:
                        print('\033[46m\033[30m▦ \033[0;0m')
                else:
                    if bloco == blocos[-1] or bloco == blocos[0]:
                        print('\033[46m\033[30m▣', end='  ')
                    else:
                        print('\033[46m\033[30m▦', end='  ')
                navioP = True
        if not navioP:
            if bloco in range(9, 100, 10):
                print('\033[46m  \033[0;0m')
            else:
                print('\033[46m ', end='  ')
            
            
#Adiciona os návios no mapa do jogo
def adicionar_navios(player):
    #Repetição para definir qual o tipo/tamanho é do barco que está sendo colocado
    for tipo, tam in carac_Navios.items():
        #Variável que define as posições disponíveis, ou seja, para impedir que o  player coloque os barcos em números aleatórios
        prox_mov = []
        #Contagem regressiva do tamanho do barco para exibir quantas partes faltam colocar
        for resto in range(tam,0,-1):
            while True:
                limpa()
                #Exibe o mapa do barco do respectivo Player
                mostrar_mapa_navios(player)
                try:
                    print('\nLegenda\n\033[46m\033[30m▦ \033[0;0m - Início ou fim de um barco\n\033[46m\033[30m▣ \033[0;0m - Corpo do barco\n\033[46m  \033[0;0m - Água')
                    print('mov',prox_mov)
                    print('nav',navios2[player][tipo])
                    posNavio = int(input(f'\nPosicione o návio {tipo}! ainda resta {resto}: '))
                    #Repetição para receber as posições dos barcos
                    for nomeNavio, posicoes in navios2[player].items():             
                        #Caso player tente colocar o barco numa posição de uso, vai retornar uma mensagem de erro
                        if posNavio in posicoes:
                            #Exibe mensagem de erro. linha 238
                            raise ValueError
                        #Verifica se o barco é igual ao tipo. Exemplo: barco 3x1 é igual ao barco 3x1
                        if nomeNavio == tipo:
                            #Caso ainda não foi colocado nenhuma posição do barco, vai guardar a posição e ordena-la alfabeticamente para futuro uso
                            if len(posicoes) == 0:   
                                navios2[player][tipo].append(posNavio)                                    
                                navios2[player][tipo] = sorted(navios2[player][tipo])
                                #Caso o barco seja horizontal
                                if tipo[0] == '1':
                                #Verificação das posições disponíveis
                                    if posNavio in range(9, 100, 10):
                                        #Caso coloque na ultima posição do eixo x, a próxima posição só poderá ser ela mesma menos 1 bloco, pois é o único lugar disponível horizontalmente
                                        prox_mov = [posicoes[0]-1]
                                    elif posNavio in range(0, 100, 10):
                                        #Caso coloque na primeira posição do eixo x, a próxima posição só poderá ser ela mesma mais 1 bloco, pois é o único lugar disponível horizontalmente.
                                        prox_mov = [posicoes[0]+1]
                                    else:
                                        #Caso coloque em qualquer posição, exceto as citadas anteriormente, o Player terá duas opções para jogar, 
                                        # 1º: posição escolhida menos 1; 
                                        # 2º: posição escolhida mais 1
                                        prox_mov = [posicoes[0]-1,posicoes[0]+1]
                                    break
                                #Caso o barco seja vertical
                                else:
                                    if posNavio in range(1, 10):
                                        #Caso coloque na primeira posição do eixo y, a próxima posição só poderá ser ela mesma mais 10 blocos, pois é o único lugar disponível verticalmente
                                        prox_mov = [posicoes[0]+10]
                                    elif posNavio in range(90, 100):
                                        #Caso coloque na ultima posição do eixo y, a próxima posição só poderá ser ela mesma menos 10 blocos, pois é o único lugar disponível verticalmente
                                        prox_mov = [posicoes[0]-10]
                                    else:
                                        #Caso coloque em qualquer posição, exceto as citadas anteriormente, o Player terá duas opções para jogar, 
                                        # 1º: posição escolhida menos 10; 
                                        # 2º: posição escolhida mais 10
                                        prox_mov = [posicoes[0]-10,posicoes[0]+10]
                                    break
                                
                            #Caso já tenha colocado a primeira posição do navio vai verificar se a ultima posição colocada é igual a ultima posição disponível. 
                            elif len(posicoes) > 0:
                                if posNavio in prox_mov:
                                    #Caso sim, adiciona a posição na lista de barcos do respectivo Player
                                    navios2[player][tipo].append(posNavio)                                   
                                    navios2[player][tipo] = sorted(navios2[player][tipo])
                                    #Caso o barco seja horizontal
                                    if tipo[0] == '1':
                                        if navios2[player][tipo][-1] in range(9, 100, 10):
                                            #Caso a ultima posição colocada esteja na ultima posição do eixo x, a próxima posição só poderá ser a primeira posição do barco menos 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios2[player][tipo][0]-1]
                                        elif navios2[player][tipo][0] in range(0, 100, 10):
                                            #Caso a ultima posição colocada esteja na primeira posição do eixo x, a próxima posição só poderá ser a ultima posição do barco mais 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios2[player][tipo][-1]+1]
                                        else:
                                            #Caso coloque em qualquer posição, exceto as citadas anteriormente, o Player terá duas opções para jogar, 
                                            # 1º: ultima posição do barco mais 1; 
                                            # 2º: primeira posição do barco menos 1
                                            prox_mov = [navios2[player][tipo][-1]+1,navios2[player][tipo][0]-1]
                                        break
                                    #Caso o barco seja vertical
                                    else:
                                        if navios2[player][tipo][0] in range(1, 10):
                                            #Caso a ultima posição colocada esteja na ultima posição do eixo y, a próxima posição só poderá ser a primeira posição do barco menos 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios2[player][tipo][-1]+10]
                                        elif navios2[player][tipo][-1] in range(90, 100):
                                            #Caso a ultima posição colocada esteja na ultima posição do eixo y, a próxima posição só poderá ser a primeira posição do barco menos 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios2[player][tipo][0]-10]
                                        else:
                                            #Caso coloque em qualquer posição, exceto as citadas anteriormente, o Player terá duas opções para jogar, 
                                            # 1º: ultima posição do barco mais 1; 
                                            # 2º: primeira posição do barco menos 1
                                            prox_mov = [navios2[player][tipo][-1]+10,navios2[player][tipo][0]-10]
                                        break
                                else:
                                    #Exibe mensagem de erro. linha 240
                                    raise TypeError
                    break
                except ValueError:
                    print("\nPosição já em uso ou valor inválido")
                    sleep(1)
                except TypeError:
                    print(f"\nNavio é {tipo}, você só pode escolher essas posições: {prox_mov}")
                    sleep(1)
                   

carac_Navios = {
        '1x3': 3,
        '3x1': 3,
        '5x1': 5,
        '1x2': 2,
        '2x1': 2,
        }
            
            
navios = {
    '1': {
        '1x3': [5, 7, 8],
        '3x1': [97, 98, 99],
        '5x1': [10, 20, 30, 40, 50],
        '1x2': [62, 63],
        '2x1': [51, 61],
        },
                 
    '2': {
        '1x3': [1, 2, 3], 
        '3x1': [9, 19, 29],
        '5x1': [48, 58, 68, 78, 88],
        '1x2': [93, 94],
        '2x1': [51, 61],
        }
     }

navios2 = {
    '1': {
        '1x3': [],
        '3x1': [],
        '5x1': [],
        '1x2': [],
        '2x1': [],
        },
                 
    '2': {
        '1x3': [], 
        '3x1': [],
        '5x1': [],
        '1x2': [],
        '2x1': [],
        }
     }

tiros = {
    '1': [],

    '2': []
         }

acertos = {'1': 0, '2': 0}
tiro_atual = 0
acerto = None

limpa()
'''
print("BATALHA NAVAL IFPE - CAMPUS PAULISTA \n")
print("=====  EQUIPE  ====== \n")
print("Pedro Hao Tavares")
print("Gleiciane Bezerra")
print("Vinicius Felipe\n\n\n")
sleep(3)
'''
print(adicionar_navios('1'))

'''
while True:
    if verificar_vencedor('1','2') ==  True:
        print ('player 1 venceu')
        break
    if verificar_vencedor('2','1') ==  True:
        print ('player 2 venceu')
        break
'''