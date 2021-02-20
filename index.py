from os import system
from time import sleep
def limpa(): return system('cls')


def verificar_vencedor(player, contra):
    global tiro_atual
    limpa()
    print('Vez do Player ',  player)
    sleep(2)
    limpa()
    while True:
        while mostrar_mapa_jogo(player, contra):
            if acertos[player] == 15:
                limpa()
                mostrar_mapa_jogo(player,contra)
                return  True
            try:
                print('\nLegenda\n▦ - Início ou fim de um barco\n▣ - Corpo do barco\n✖ - Tiro errado\n▢ - Água')
                if acerto:
                    print('\nJogue Novamente')
                tiro_atual = int(input('\n\nDigite uma coordenada (Ex: 3,0): ').replace(',',''))
                if tiro_atual in tiros[player]:
                    tiro_atual = None
                    raise ValueError
                tiros[player].append(tiro_atual)
            except:
                print("Posição já usada ou valor inválido")
        break
    mostrar_mapa_jogo(player, contra)
    sleep(3)
    return False


def mostrar_mapa_jogo(player, contra):
    global acertos, tiros, navios, tiro_atual, acerto
    limpa()
    tiro =  False
    print('   0  1  2  3  4  5  6  7  8  9')
    acertos[player] = 0
    for bloco in range(100):
        if bloco in range(0, 100, 10):
            print(int(bloco/10), end='  ')
        if bloco in tiros[player]:
            for navio, blocos in navios[contra].items():
                if bloco in blocos:
                    acertos[player] += 1
                    if bloco in range(9, 100, 10):
                        if bloco == blocos[-1] or bloco == blocos[0]:
                            print('▦')
                        else:
                            print('▣')
                    else:
                        if bloco == blocos[-1] or bloco == blocos[0]:
                            print('▦', end='  ')
                        else:
                            print('▣', end='  ')
                    if bloco == tiro_atual:
                        tiro = True
                        acerto =  True
                    break
                elif navio == '2x1':
                    if bloco in range(9, 100, 10):
                        print('✖')
                    else:
                        print('✖', end='  ')
                    if bloco == tiro_atual:
                        tiro =  True
                        acerto = False
                    break
        elif bloco in range(9, 100, 10):
            print('▢')
        else:
            print('▢', end='  ')
    if tiro:
        return acerto
    return True        


def mostrar_mapa_navios(player):
    print('   0  1  2  3  4  5  6  7  8  9')
    for bloco in range(100):
        navioP = False
        if bloco in range(0, 100, 10):
            print(int(bloco/10), end='  ')
        for  blocos in navios2[player].values():
            if bloco in blocos:
                if bloco in range(9, 100, 10):
                    if bloco == blocos[-1] or bloco == blocos[0]:
                        print('▦')
                    else:
                        print('▣')
                else:
                    if bloco == blocos[-1] or bloco == blocos[0]:
                        print('▦', end='  ')
                    else:
                        print('▣', end='  ')
                navioP = True
        if not navioP:
            if bloco in range(9, 100, 10):
                print('▢')
            else:
                print('▢', end='  ')
            
            
            
def adicionar_navios(player):
    for tipo, tam in carac_Navios.items():
        prox_mov = []
        for resto in range(tam,0,-1):
            while True    :
                limpa()
                mostrar_mapa_navios(player)
                try:
                    print('\nLegenda\n▦ - Início ou fim de um barco\n▣ - Corpo do barco\n✖ - Tiro errado\n▢ - Água')
                    print('mov',prox_mov)
                    print('nav',navios2[player][tipo])
                    posNavio = int(input(f'\nPosicione o návio {tipo}! ainda resta {resto}: '))
                    
                    for nomeNavio, posicoes in navios2[player].items():              
                        if posNavio in posicoes:
                            raise ValueError
                        if tipo[0] == '1':
                            if nomeNavio == tipo:
                                if len(posicoes) == 0:   
                                    navios2[player][tipo].append(posNavio)                                    
                                    navios2[player][tipo] = sorted(navios2[player][tipo])
                                    if posNavio in range(9, 100, 10):
                                        prox_mov = [posicoes[0]-1]
                                    elif posNavio in range(0, 100, 10):
                                        prox_mov = [posicoes[0]+1]
                                    else:
                                        prox_mov = [posicoes[0]-1,posicoes[0]+1]
                                    break
            
                                elif len(posicoes) > 0:
                                    if posNavio in prox_mov:
                                        navios2[player][tipo].append(posNavio)                                    
                                        navios2[player][tipo] = sorted(navios2[player][tipo])
                                        if navios2[player][tipo][-1] in range(9, 100, 10):
                                            prox_mov = [navios2[player][tipo][0]-1]
                                        elif navios2[player][tipo][0] in range(0, 100, 10):
                                            prox_mov = [navios2[player][tipo][-1]+1]
                                        else:
                                            prox_mov = [navios2[player][tipo][-1]+1,navios2[player][tipo][0]-1]
                                        break
                                    else:
                                        raise TypeError
                        else:
                            if nomeNavio == tipo:
                                if len(posicoes) == 0:   
                                    navios2[player][tipo].append(posNavio)                                    
                                    navios2[player][tipo] = sorted(navios2[player][tipo])
                                    if posNavio in range(9, 100, 10):
                                        prox_mov = [posicoes[0]-1]
                                    elif posNavio in range(0, 100, 10):
                                        prox_mov = [posicoes[0]+1]
                                    else:
                                        prox_mov = [posicoes[0]-1,posicoes[0]+1]
                                    break
            
                                elif len(posicoes) > 0:
                                    if posNavio in prox_mov:
                                        navios2[player][tipo].append(posNavio)                                    
                                        navios2[player][tipo] = sorted(navios2[player][tipo])
                                        if navios2[player][tipo][-1] in range(9, 100, 10):
                                            prox_mov = [navios2[player][tipo][0]-1]
                                        elif navios2[player][tipo][0] in range(0, 100, 10):
                                            prox_mov = [navios2[player][tipo][-1]+1]
                                        else:
                                            prox_mov = [navios2[player][tipo][-1]+1,navios2[player][tipo][0]-1]
                                        break
                                    else:
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