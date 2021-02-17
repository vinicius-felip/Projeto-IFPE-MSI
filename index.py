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
            if acertos[player] == 14:
                limpa()
                mostrar_mapa_jogo(player,contra)
                return  True
            try:
                tiro_atual = int(input('\n\nDigite uma coordenada (Ex: 3,0): ').replace(',',''))
                if tiro_atual in tiros[player]:
                    tiro_atual = None
                    raise ValueError
                tiros[player].append(tiro_atual)
            except:
                print("Digite um valor válido")
        break
    mostrar_mapa_jogo(player, contra)
    sleep(3)
    return False


def mostrar_mapa_jogo(player, contra):
    global acertos, tiros, navios, tiro_atual
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
        if bloco in range(0, 100, 10):
            print(int(bloco/10), end='  ')
        if bloco in tiros[player]:
            for navio, blocos in navios[player].items():
                if bloco in blocos:
                    if bloco in range(9, 100, 10):
                        if bloco == blocos[-1] or bloco == blocos[0]:
                            print('Z')
                        else:
                            print('X')
                    else:
                        if bloco == blocos[-1] or bloco == blocos[0]:
                            print('Z', end='  ')
                        else:
                            print('X', end='  ')
                    break
                elif navio == '2x1':
                    if bloco in range(9, 100, 10):
                        print('A')
                    else:
                        print('A', end='  ')
                    break
        elif bloco in range(9, 100, 10):
            print('▢')
        else:
            print('▢', end='  ')
            
            
navios = {
    '1': {
        '1x3': [5, 7, 8],
        '5x1': [10, 20, 30, 40, 50],
        '2x2': [45, 46, 55, 56],
        '2x1': [62, 63]
        },
                 
    '2': {
        '1x3': [1, 2, 3], 
        '5x1': [48, 58, 68, 78, 88], 
        '2x2': [20, 21, 30, 31],
        '2x1': [93, 94]
        }
     }

tiros = {
    '1': [],

    '2': []
         }

acertos = {'1': 0, '2': 0}
tiro_atual = 0

limpa()
print("BATALHA NAVAL IFPE - CAMPUS PAULISTA \n")
print("=====  EQUIPE  ====== \n")
print("Pedro Hao Tavares")
print("Gleiciane Bezerra")
print("Vinicius Felipe\n\n\n")
sleep(3)
while True:
    if verificar_vencedor('1','2') ==  True:
        print ('player 1 venceu')
        break
    if verificar_vencedor('2','1') ==  True:
        print ('player 2 venceu')
        break
