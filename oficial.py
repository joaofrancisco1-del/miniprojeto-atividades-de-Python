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
def placar(a,b):
    if a == 3 and b < 3:
        print("JOGADOR 1 VENCEU!")
        print()
    if b == 3 and a < 3:
        print("JOGADOR 2 VENCEU!")
        print()

    print("          PLACAR")
    print(f"JOGADOR 1: {a} x {b} :JOGADOR 2")
print("JOGO DA VELHA")#começo do jogo
sair = False
ctr = 0
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
#faltando corrigir as jogadas onde a posição ja esta ocupada!!!
while True:
    resultado(matriz)
    print()
    a1 = str(input("DIGITE SEU CARACTER JOGADOR 1: "))
    a2 = str(input("DIGITE SEU CARACTER JOGADOR 2: "))
    pont1 = 0
    pont2 = 0
    ctr=1
    z = 0
    for x in range(1,10):
        if x % 2 != 0:
            c = 0
            while True:
                pos1 = str(input("DIGITE SUA JOGADA JOGADOR 1: "))
                print()
                if tde(a1,pos1,matriz) == 0:
                    break
                else:
                    print("DIGITE UMA JOGADA VÁLIDA")
                    print()
            jogada1(a1,pos1,matriz)
            resultado(matriz)
            print()
        if teste(matriz,c) != 0:
            pont1+=1
            break
        if x % 2 == 0:
            c = 0
            while True:
                pos2 = str(input("DIGITE SUA JOGADA JOGADOR 2: "))
                print()
                if tde(a2,pos2,matriz) == 0:
                    break
                else:
                    print("DIGITE UMA JOGADA VÁLIDA")
                    print()
            jogada1(a2,pos2,matriz)
            resultado(matriz)
            print()
        if teste(matriz,c) != 0:
            pont2+=1
            break
    placar(pont1,pont2)
    continuar=input('QUER CONTINUAR JOGANDO? (S OU N)').lower()
    if continuar=='n':
        break
    matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]