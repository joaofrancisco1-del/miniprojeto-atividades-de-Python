#JOGO DA VELHA
#EQUIPE: JOAO LUCAS, LUIZ NETO (TRABALHAMOS IGUALMENTE, DIVIDINDO MEIO A MEIO AS TAREFAS)
def jogada1(a,b,matriz):
    jogue=[]
    c = 0
    for p in b:
        if c == 2:
            break
        jogue.append(p)
        c += 1
    for r in jogue:
        if r == 'a' or r == "A":
            jogue[1]= 0
        if r == 'b' or r == "B":
            jogue[1]= 1
        if  r == 'c' or r == "C":
            jogue[1]= 2
        if r == '1':
            jogue[0]= 0
        if r == '2':
            jogue[0]= 1
        if  r == '3':
            jogue[0]= 2
    i = jogue[0]
    j = jogue[1]
    if matriz[i][j] == " ":
        matriz[i][j] = a
        
def tde(a,b,matriz): #ver se a jogada é válida
    f = 0
    jogue=[]
    c = 0
    for p in b:
        if c == 2:
            break
        jogue.append(p)
        c += 1
    for r in jogue:
        if r == 'a' or r == "A":
            jogue[1]= 0
        if r == 'b' or r == "B":
            jogue[1]= 1
        if  r == 'c' or r == "C":
            jogue[1]= 2
        if r == '1':
            jogue[0]= 0
        if r == '2':
            jogue[0]= 1
        if  r == '3':
            jogue[0]= 2
    if (jogue [1] != 0 and jogue [1] != 1 and jogue [1] != 2):
        f += 1
    if (jogue [1] == 0 or jogue [1] == 1 or jogue [1] == 2):
        i = jogue[0]
        j = jogue[1]
        if matriz[i][j] != " ":
            f += 1  
    return f

def resultado(matriz):#jogo da velha
    print("   A   B   C")

    for i in range(len(matriz)):
        print(" ", end = "")
        if i == 0:
            print("1", end = " ")
        if i == 1:
            print("2", end = " ")
        if i == 2:
            print("3", end = " ")
        for j in range(len(matriz[0])):
            print(matriz[i][j], end = "")
            if j != 2:
                print(" | ", end = "")
        print()
        if i != 2:
            print("  ---+---+---")
            
def teste(matriz,b):
    if matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2] and matriz[0][1] == matriz[0][2] and matriz[0][0] != " " and matriz[0][1] != " " and matriz[0][2] != " ":
        b += 1
    elif matriz[0][0] == matriz[1][0] and matriz[0][0] == matriz[2][0] and matriz[1][0] == matriz[2][0] and matriz[0][0] != " " and matriz[1][0] != " " and matriz[2][0] != " ":
        b += 1  
    elif matriz[0][1] == matriz[1][1] and matriz[0][0] == matriz[2][1] and matriz[1][1] == matriz[2][1] and matriz[0][1] != " " and matriz[1][1] != " " and matriz[2][1] != " ":
        b += 1
    elif matriz[0][2] == matriz[1][2] and matriz[0][2] == matriz[2][2] and matriz[1][2] == matriz[2][2] and matriz[0][2] != " " and matriz[1][2] != " " and matriz[2][2] != " ":
        b += 1
    elif matriz[1][0] == matriz[1][1] and matriz[1][0] == matriz[1][2] and matriz[1][1] == matriz[1][2] and matriz[1][0] != " " and matriz[1][1] != " " and matriz[1][2] != " ":
        b += 1
    elif matriz[2][0] == matriz[2][1] and matriz[2][0] == matriz[2][2] and matriz[2][1] == matriz[2][2] and matriz[2][0] != " " and matriz[2][1] != " " and matriz[2][2] != " ":
        b += 1
    elif matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2] and matriz[1][1] == matriz[2][2] and matriz[0][0] != " " and matriz[1][1] != " " and matriz[2][2] != " ":
        b += 1
    elif matriz[0][2] == matriz[1][1] and matriz[0][2] == matriz[2][0] and matriz[1][1] == matriz[2][0] and matriz[0][2] != " " and matriz[1][1] != " " and matriz[2][0] != " ":
        b += 1
    return b

def placar(x,z,c,d): #x e z sao as pontuações,
    if x >= 1 or x > z:
        print("          JOGADOR 1 VENCEU A RODADA")
        print()
    elif z >= 1 or z > x:
        print("          JOGADOR 2 VENCEU A RODADA")
        print()
    else:
        print("             A RODADA EMPATOU")
    print("                   PLACAR")
    print()
    print(f"    JOGADOR 1 ({c}): {x} x {z} : ({d}) JOGADOR 2")
    
print("JOGO DA VELHA")#começo do jogo
sair = False
ctr = 0
jp1 = 0
jp2 = 0
pont1 = 0
pont2 = 0
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
resultado(matriz)
while True:
    print()
    a1 = str(input("DIGITE SEU CARACTER JOGADOR 1: "))
    z = 0
    for r in a1:
        if r == " ":
            print("DIGITE UM CARACTER VÁLIDO")
            print()
            resultado(matriz)
            print()
            z += 1
            break
    if z != 0:
        continue
    a2 = str(input("DIGITE SEU CARACTER JOGADOR 2: "))
    z = 0
    for r in a2:
        if r == " ":
            print("DIGITE UM CARACTER VÁLIDO")
            print()
            resultado(matriz)
            print()
            z += 1
            break
    if z != 0 or a2 in a1:
        continue
    print()
    resultado(matriz)
    print()
    for x in range(1,10):
        if x % 2 != 0:
            jp1 = 0
            while True:
                pos1 = str(input("DIGITE SUA JOGADA JOGADOR 1: "))
                print()
                
                if tde(a1,pos1,matriz) == 0:
                    break
                else:
                    print("DIGITE UMA JOGADA VÁLIDA")
                    print()
                    resultado(matriz)
                    print()
            jogada1(a1,pos1,matriz)
            resultado(matriz)
            print()
        if teste(matriz,jp1) != 0:
            pont1 += 1
            break
        if x % 2 == 0:
            jp2 = 0
            while True:
                pos2 = str(input("DIGITE SUA JOGADA JOGADOR 2: "))
                print()
                if tde(a2,pos2,matriz) == 0:
                    break
                else:
                    print("DIGITE UMA JOGADA VÁLIDA")
                    print()
                    resultado(matriz)
                    print()
            jogada1(a2,pos2,matriz)
            resultado(matriz)
            print()
        if teste(matriz,jp2) != 0:
            pont2+=1
            break
    placar(pont1,pont2,a1,a2)
    print()
    continuar=input('QUER CONTINUAR JOGANDO? (S OU N) ').lower()
    print()
    if continuar in "n":
        break
    matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]