#joao lucas e luiz neto eng.comp
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
            
def placar(a,b,d):
    if a == 3 and b < 3:
        print("JOGADOR 1 VENCEU!")
        print()
    if a == 3 and b < 3:
        print("JOGADOR 2 VENCEU!")
        print()

    print("          PLACAR")
    print(f"JOGADOR 1: {a} x {b} :JOGADOR 2")
        
'''x = [[1,2,3], [4,5,6], [7,8,9]]
z = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
y = z
resultado(z)
a = " "
a1 = str(input("DIGITE SEU CARACTER JOGADOR 1: "))
a2 = str(input("DIGITE SEU CARACTER JOGADOR 2: "))'''
sair = False
while True:

    if a == 3 or b == 3:
        cond = str(input("DESEJA CONTINUAR? ").lower())
        if cond == "s":
            sair = False
        if cond == "n":
            sair = True
    if sair:
        break
    
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
            
def placar(a,b,d):
    if a == 3 and b < 3:
        print("JOGADOR 1 VENCEU!")
        print()
    if a == 3 and b < 3:
        print("JOGADOR 2 VENCEU!")
        print()

    print("          PLACAR")
    print(f"JOGADOR 1: {a} x {b} :JOGADOR 2")

    
print("JOGO DA VELHA")
while True:
    a1 = str(input("DIGITE SEU CARACTER JOGADOR 1: "))
    a2 = str(input("DIGITE SEU CARACTER JOGADOR 2: "))
    while True:
    pos1=input('').split().lower()
    pos2=input('').split().lower()
    
    if matriz[x][x] ==  and matriz[x][x] and matriz
    
def teste(matriz,ctr):
    if matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2] and matriz[0][1] == matriz[0][2]:
        ctr += 1
    if matriz[0][0] == matriz[1][0] and matriz[0][0] == matriz[2][0] and matriz[1][0] == matriz[2][0]:
        ctr += 1  
    if matriz[0][1] == matriz[1][1] and matriz[0][0] == matriz[2][1] and matriz[1][1] == matriz[2][1]:
        ctr += 1
    
    if matriz[0][2] == matriz[1][2] and matriz[0][2] == matriz[2][2] and matriz[1][2] == matriz[2][2]:
        ctr += 1
    if matriz[1][0] == matriz[1][1] and matriz[1][0] == matriz[1][2] and matriz[1][1] == matriz[1][2]:
        ctr += 1
        
    if matriz[2][0] == matriz[2][1] and matriz[2][0] == matriz[2][2] and matriz[2][1] == matriz[2][2]:
        ctr += 1
    
    if matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2] and matriz[1][1] == matriz[2][2]:
        ctr += 1
        
    if matriz[0][2] == matriz[1][1] and matriz[0][2] == matriz[2][0] and matriz[1][1] == matriz[2][0]:
        ctr += 1
        
def jogada1(a,b,matriz):
    for x in range(len(b)):
        if b[i] == 'a':
            b.replace("a", 0)
        if b[i] == 'b':
            b.replace("b", 1)
        if  b[i] == 'c':
            b.replace("c", 2)
    if matriz[b[0]b[1]] == " ":
        matriz[b[0]b[1]] = a
        
print("JOGO DA VELHA")
sair = False
ctr = 0
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
while True:
    a1 = str(input("DIGITE SEU CARACTER JOGADOR 1: "))
    a2 = str(input("DIGITE SEU CARACTER JOGADOR 2: "))
    while True:
        pos1 = str(input('')).split().lower()
        jogada1(a1,pos1,matriz)
        resultado(matriz)
