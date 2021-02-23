from os import system
from time import sleep
import random
def limpa(limpar=True): 
    if limpar: 
        return system('cls')


#Função que verifica quais os próximos tiros que o bot irá dar de acordo com as posições disponiveis e quais as chances de acertar um navío
def verificar_tiro(tiros,local_acerto,chance_tiro_acerto):
    #Váriavel que é a posição dos navíos do Player 1
    global naviosP1
    #Lista temporária para definir as posições disponiveis
    numtemporario = []
    numtemporario.extend(local_acerto)
    #Verifica se as posições próximas disponiveis já foi atingida pelo BOT, caso sim, irá remove-la das opções
    for num in numtemporario:
        if num in tiros:
            local_acerto.remove(num) 
    #Verifica as posições dos barcos e define qual a chance de atingi-lo caso esteja próximo do ultimo acerto
    for num in local_acerto:
        if num in naviosP1:
            chance_tiro_acerto.append(10)
        else:
            chance_tiro_acerto.append(1)   
            
    
#Função para dar "inteligencia" ao BOT
def tiro_IA(acerto):
    #Variaveis que são necessárias para a execução do código
    global tiro_atual, local_acerto, tiros, naviosP1
    #Listas que define qual bloco tem mais chance de ser hitado pelo BOT
    chance_tiro_acerto = list()
    chance_tiro = list()
    #Lista que define os o minimo e maximo de blocos que podem ser hitados
    tiros_disponivel = list(range(0,100))
    #Condição para saber se o BOT já atirou. Caso sim, irá remover a posição da lista de tiros disponiveis
    if len(tiros['IA'])>0:
        for num in tiros['IA']:
            if num in tiros_disponivel:
                tiros_disponivel.remove(num)
    #Aumenta a chance de atirar na posição se o bloco for o navío do Player
    for num in tiros_disponivel:
        if num in naviosP1:
            chance_tiro.append(10)
        else:
            chance_tiro.append(1)
    print('\nIA está escolhendo...')  
    sleep(2)
    #Caso não o BOT não tenha acertado o ultimo tiro, irá atirar randomicamente, mas com maior chance de atirar em alguma posição de navío
    if not acerto:
        tiro_atual = random.choices(tiros_disponivel, weights= chance_tiro, k=1)[0]
    #Caso tenha acertado
    else:
        #Define o proximo tiro do BOT de acordo com o ultimo acerto dado, deixando apenas posições próximas do ultimo tiro
        if tiro_atual in range(0,10):
            #Caso o ultimo tiro tenha sido na posição 0,0, o bot só poderá atirar na posições 1 ou 10(com mais chance de atigir a posição do navío, caso exista)
            if tiro_atual == 0:
                local_acerto = [tiro_atual+1,tiro_atual+10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
            #Caso o ultimo tiro tenha sido na posição 0,9, o bot só poderá atirar nas posições 8 ou 19(com mais chance de atigir a posição do navío, caso exista)
            elif tiro_atual == 9:
                local_acerto = [tiro_atual-1,tiro_atual+10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
            #Caso o ultimo tiro tenha sido em qualquer posição da primeira linha, exceto as citadas antes, poderá atirar nas posições +10, -1 e +1(com mais chance de atigir a posição do navío, caso exista)
            else:
                local_acerto = [tiro_atual+1,tiro_atual-1,tiro_atual+10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
        #Caso o ultimo tiro tenha sido em qualquer posição da primeira coluna, exceto posição 90 e 0, poderá atirar nas posições +10, -10 e +1(com mais chance de atigir a posição do navío, caso exista)
        elif tiro_atual in range(10, 90, 10):
                local_acerto = [tiro_atual+1,tiro_atual-10, tiro_atual+10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
        elif tiro_atual in range(90,100):
            #Caso o ultimo tiro tenha sido na posição 9,0, o bot só poderá atirar na posições 91 ou 80(com mais chance de atigir a posição do navío, caso exista)
            if tiro_atual == 90:
                local_acerto = [tiro_atual+1,tiro_atual-10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
            #Caso o ultimo tiro tenha sido na posição 9,9, o bot só poderá atirar na posições 98 ou 89(com mais chance de atigir a posição do navío, caso exista
            elif tiro_atual == 99:
                local_acerto = [tiro_atual-1,tiro_atual-10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
            #Caso o ultimo tiro tenha sido em qualquer posição da ultima linha, exceto as citadas antes, poderá atirar nas posições -10, -1 e +1(com mais chance de atigir a posição do navío, caso exista)
            else:
                local_acerto = [tiro_atual+1,tiro_atual-1,tiro_atual-10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
        #Caso o ultimo tiro tenha sido em qualquer posição da ultima coluna, exceto posição 9 e 99, poderá atirar nas posições +10, -10 e -1(com mais chance de atigir a posição do navío, caso exista)
        elif tiro_atual in range(19, 100, 10):
                local_acerto = [tiro_atual-1,tiro_atual-10, tiro_atual+10]
                verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
        #Caso o ultimo tiro tenha sido em qualquer posição do mapa, exceto todas citadas antes, poderá atirar nas posições +10, -10, -1 e +1(com mais chance de atigir a posição do navío, caso exista)
        else:
            local_acerto = [tiro_atual-1,tiro_atual+1,tiro_atual-10, tiro_atual+10]
            verificar_tiro(tiros['IA'],local_acerto, chance_tiro_acerto)
        if not len(local_acerto) == 0:
            #Executa o tiro de acordo com todas as regras ditadas pelos IFs e pelo verificar_tiro(). linha 5
            tiro_atual = random.choice(local_acerto)
        else:
            #Caso a função de definir os blocos disponiveis retorne uma lista zerada, o proximo tiro do BOT será aleatório. linha 5
            tiro_atual = random.choices(tiros_disponivel, weights= chance_tiro, k=1)[0]


#Exibe uma mensagem no jogo
def espere(frase):
    limpa()
    print(f'{frase}.')
    sleep(1)
    limpa()
    print(f'{frase}..')
    sleep(1)
    limpa()
    print(f'{frase}...')
    sleep(1)
    limpa()


#Função das regras
def exibir_sobre_regras():
    print('''\033[47m\033[30m
Sobre/Regras

O jogo consiste em posicionar seus navíos em um tabuleiro 10x10 e tentar acertar o navío do seu adversário.

- Jogador 1 é sempre o primeiro a jogar e posicionar navíos;
- A ordem para posicionar os navíos são sempre as mesmas: 1x3, 3x1, 5x1, 2x1, 1x2;
- Não existe limite de tiros ou tempo;
- O vencedor é o primeiro a derrubar todos os navíos

\033[0;0m''')
    input('Pressione ENTER para voltar')
    main()
    
    
    
def iniciar_jogo_PVIA():
    global navios, naviosP1
    #Mensagem exibida ao iniciar o jogo
    espere('Iniciando o Jogo')
    #Sistema de adicionar os navíos do player
    adicionar_navios('1')
    #Salva a posição dos navíos do player numa lista para ajudar o BOT
    for num in navios['1'].values():
        naviosP1.extend(num)
    #Jogo iniciado a partir de uma repetição. Quando uma condição for verdadeira, o jogo para e é exibido uma mensagem informando o vencedor
    while True:
        #Função para verificar se o player 1 é o vencedor
        if verificar_vencedor('1','IA') ==  True:
            print ('\n\n\t Player 1 venceu\n\n')
            if input('Jogar novamente? [S/N] ').upper() in 'S':
                main()
            exit
        #Função para verificar se a IA é o vencedor
        if verificar_vencedor('IA','1') ==  True:
            print ('\n\n\t IA venceu\n\n')
            if input('Jogar novamente? [S/N] ').upper() in 'S':
                main()
            exit


def iniciar_jogo_PVP():
    #Mensagem exibida ao iniciar o jogo
    espere('Iniciando o Jogo')
    #Sistema de adicionar os navíos de cada Player
    adicionar_navios('1')
    adicionar_navios('2')
    #Jogo iniciado a partir de uma repetição. Quando uma condição for verdadeira, o jogo para e é exibido uma mensagem informando o vencedor
    while True:
        #Função para verificar se o player 1 é o vencedor
        if verificar_vencedor('1','2') ==  True:
            print ('\n\n\t Player 1 venceu\n\n')
            if input('Jogar novamente? [S/N] ').upper() in 'S':
                main()
            exit
        #Função para verificar se o player 2 é o vencedor
        if verificar_vencedor('2','1') ==  True:
            print ('\n\n\t Player 2 venceu\n\n')
            if input('Jogar novamente? [S/N] ').upper() in 'S':
                main()
            exit


#Função para verificar o vencedor
def verificar_vencedor(player, contra):
    global tiro_atual, local_acerto
    espere(f'Vez do Player {player}')
    while True:
        #Executa a função de mostrar mapa com return padrão True, caso player erre um tiro, return se torna False
        while mostrar_mapa_jogo(player, contra):
            #Verifica se o Player é o vencedor pela contagem de tiros acertados
            if acertos[player] == 15:
                limpa()
                print(f'\n\tTiros do Player {contra}')
                mostrar_mapa_jogo(contra,player, False)
                print(f'\n\tTiros do Player {player}')
                mostrar_mapa_jogo(player,contra, False)
                #Caso exista um vencedor, função verificar_vencedor() retorna True, satisfazendo o IF inicial
                return  True
            try:
                print('\nLegenda\n\033[46m\033[30m▦ \033[0;0m - Início ou fim de um barco\n\033[46m\033[30m▣ \033[0;0m - Corpo do barco\n\033[46m\033[31m✖ \033[0;0m - Tiro errado\n\033[46m  \033[0;0m - Água')
                if player == 'IA':
                    tiro_IA(acerto)
                else:
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
def mostrar_mapa_jogo(player, contra, fim_jogo = True):
    global acertos, tiros, navios, tiro_atual, acerto, local_acerto
    local_acerto = []
    limpa(fim_jogo)
    #Variáves que são necessárias para exibição do mapa
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
            print(int(bloco/10), end='   ')
        for  blocos in navios[player].values():
            if bloco in blocos:
                if bloco in range(9, 100, 10):
                    if bloco == blocos[-1] or bloco == blocos[0]:
                        print('\033[46m\033[30m▦ \033[0;0m')
                    else:
                        print('\033[46m\033[30m▣ \033[0;0m')
                else:
                    if bloco == blocos[-1] or bloco == blocos[0]:
                        print('\033[46m\033[30m▦', end='  ')
                    else:
                        print('\033[46m\033[30m▣', end='  ')
                navioP = True
        if not navioP:
            if bloco in range(9, 100, 10):
                print('\033[46m  \033[0;0m')
            else:
                print('\033[46m ', end='  ')
            
            
#Adiciona os návios no mapa do jogo
def adicionar_navios(player):
    espere(f'Vez do Player {player} posicionar os navíos')
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
                    posNavio = int(input(f'\nAinda restam {resto} partes!\nPosicione o návio {tipo} em uma coordenada (Ex: 3,0): ').replace(',',''))
                    #Repetição para receber as posições dos barcos
                    for nomeNavio, posicoes in navios[player].items():             
                        #Caso player tente colocar o barco numa posição de uso, vai retornar uma mensagem de erro
                        if posNavio in posicoes:
                            #Exibe mensagem de erro. linha 238
                            raise ValueError
                        #Verifica se o barco é igual ao tipo. Exemplo: barco 3x1 é igual ao barco 3x1
                        if nomeNavio == tipo:
                            #Caso ainda não foi colocado nenhuma posição do barco, vai guardar a posição e ordena-la alfabeticamente para futuro uso
                            if len(posicoes) == 0:   
                                navios[player][tipo].append(posNavio)                                    
                                navios[player][tipo] = sorted(navios[player][tipo])
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
                                    navios[player][tipo].append(posNavio)                                   
                                    navios[player][tipo] = sorted(navios[player][tipo])
                                    #Caso o barco seja horizontal
                                    if tipo[0] == '1':
                                        if navios[player][tipo][-1] in range(9, 100, 10):
                                            #Caso a ultima posição colocada esteja na ultima posição do eixo x, a próxima posição só poderá ser a primeira posição do barco menos 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios[player][tipo][0]-1]
                                        elif navios[player][tipo][0] in range(0, 100, 10):
                                            #Caso a ultima posição colocada esteja na primeira posição do eixo x, a próxima posição só poderá ser a ultima posição do barco mais 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios[player][tipo][-1]+1]
                                        else:
                                            #Caso coloque em qualquer posição, exceto as citadas anteriormente, o Player terá duas opções para jogar, 
                                            # 1º: ultima posição do barco mais 1; 
                                            # 2º: primeira posição do barco menos 1
                                            prox_mov = [navios[player][tipo][-1]+1,navios[player][tipo][0]-1]
                                        break
                                    #Caso o barco seja vertical
                                    else:
                                        if navios[player][tipo][0] in range(1, 10):
                                            #Caso a ultima posição colocada esteja na ultima posição do eixo y, a próxima posição só poderá ser a primeira posição do barco menos 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios[player][tipo][-1]+10]
                                        elif navios[player][tipo][-1] in range(90, 100):
                                            #Caso a ultima posição colocada esteja na ultima posição do eixo y, a próxima posição só poderá ser a primeira posição do barco menos 1 bloco, pois é o único lugar disponível horizontalmente
                                            prox_mov = [navios[player][tipo][0]-10]
                                        else:
                                            #Caso coloque em qualquer posição, exceto as citadas anteriormente, o Player terá duas opções para jogar, 
                                            # 1º: ultima posição do barco mais 1; 
                                            # 2º: primeira posição do barco menos 1
                                            prox_mov = [navios[player][tipo][-1]+10,navios[player][tipo][0]-10]
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
                    sleep(2)
    limpa()
    #Exibe o mapa quando todos os navios forem posicionados
    mostrar_mapa_navios(player)
    print('\nTodos os Barcos foram posicionados')
    sleep(2)              
    
    
    
def main():
    while True:
        limpa()
        print("BATALHA NAVAL IFPE - CAMPUS PAULISTA \n")
        print("=====  EQUIPE  ====== \n")
        print("Pedro Hao Tavares")
        print("Gleiciane Bezerra")
        print("Vinicius Felipe\n\n\n")
        print('\n\n0 - Iniciar Jogo\n1 - Sobre/Regras\n2 - Sair')
        try:
            opc = input('\n\nDigite uma opção: ')
            if opc in '012':
                if opc == '0':
                    while True:
                        limpa()
                        try:
                            print("BATALHA NAVAL IFPE - CAMPUS PAULISTA \n")
                            print("=====  EQUIPE  ====== \n")
                            print("Pedro Hao Tavares")
                            print("Gleiciane Bezerra")
                            print("Vinicius Felipe\n\n\n")
                            print('\n\n0 - Jogar contra amigo\n1 - Jogar contra máquina\n2 - Voltar')
                            opc = input('\n\nDigite uma opção: ')
                            if opc in '012':
                                if opc == '0':
                                    iniciar_jogo_PVP()
                                if opc == '1':
                                    iniciar_jogo_PVIA()
                                if opc == '2':
                                    main()
                                break
                            raise ValueError  
                        except ValueError:
                            print('Valor inválido')
                            sleep(1)
                if opc == '1':
                    exibir_sobre_regras()
                if opc == '2':
                    exit
                break
            raise ValueError
        except ValueError:
            print('Valor inválido')
            sleep(1)
            
            
#------------------------------------------VARIAVEIS GLOBAIS    
local_acerto = []
naviosP1 = []

#Caracteristicas dos navios
carac_Navios = {
        '1x3': 3,
        '3x1': 3,
        '5x1': 5,
        '1x2': 2,
        '2x1': 2,
        }
            
#Navios posicionados pelos players            
navios = {
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
        },
    
    'IA': {
        '1x3': [97, 98, 99], 
        '3x1': [21, 31, 41],
        '5x1': [46, 56, 66, 76, 86],
        '1x2': [82, 83],
        '2x1': [9, 19],
    }
     }

#Tiros de cada player/IA
tiros = {
    '1': [],

    '2': [],
    
    'IA': []
         }
#Contagem de acertos para definir o vencedor
acertos = {'1': 0, '2': 0, 'IA': 0}
#Ultimo tiro dado pelo Player
tiro_atual = 0
acerto = None
#--------------------------------------------------------

            
#Inicia o código
if __name__ == '__main__':
    main()