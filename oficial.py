def jogada1(a,b,matriz,f):
    jogue=[]
    for p in b:
        jogue.append(p)
    for r in jogue:
        if r == 'a':
            jogue[1]= 0
        if r == 'b':
            jogue[1]= 1
        if  r == 'c':
            jogue[1]= 2
        if r == '1':
            jogue[0]= 0
        if r == '2':
            jogue[0]= 1
        if  r == '3':
            jogue[0]= 2
    i = jogue[0]
    j = jogue[1]
    if matriz[i][j] != " ":
        f += 1
    elif matriz[i][j] == " ":
        matriz[i][j] = a
    
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
    x = 0
    if matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2] and matriz[0][1] == matriz[0][2]:
        x += 1
    if matriz[0][0] == matriz[1][0] and matriz[0][0] == matriz[2][0] and matriz[1][0] == matriz[2][0]:
        x += 1  
    if matriz[0][1] == matriz[1][1] and matriz[0][0] == matriz[2][1] and matriz[1][1] == matriz[2][1]:
        x += 1
    
    if matriz[0][2] == matriz[1][2] and matriz[0][2] == matriz[2][2] and matriz[1][2] == matriz[2][2]:
        x += 1
    if matriz[1][0] == matriz[1][1] and matriz[1][0] == matriz[1][2] and matriz[1][1] == matriz[1][2]:
        x += 1
        
    if matriz[2][0] == matriz[2][1] and matriz[2][0] == matriz[2][2] and matriz[2][1] == matriz[2][2]:
        x += 1
    
    if matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2] and matriz[1][1] == matriz[2][2]:
        x += 1
        
    if matriz[0][2] == matriz[1][1] and matriz[0][2] == matriz[2][0] and matriz[1][1] == matriz[2][0]:
        x += 1
    if x != 0:
        b += 1
def placar(a,b):
    if a == 3 and b < 3:
        print("JOGADOR 1 VENCEU!")
        print()
    if a == 3 and b < 3:
        print("JOGADOR 2 VENCEU!")
        print()

    print("          PLACAR")
    print(f"JOGADOR 1: {a} x {b} :JOGADOR 2")
print("JOGO DA VELHA")
sair = False
ctr = 0
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
while True:
    resultado(matriz)
    a1 = str(input("DIGITE SEU CARACTER JOGADOR 1: "))
    a2 = str(input("DIGITE SEU CARACTER JOGADOR 2: "))
    pont1 = 0
    pont2 = 0
    ctr=1
    z = 0
    for x in range(9):
        if ctr%2!=0:
            while True:
                d = 0
                pos1 = str(input("DIGITE SUA JOGADA JOGADOR 1: "))
                jogada1(a1,pos1,matriz,d)
                if d != 0:
                    break
                else:
                    print("DIGITE UMA JOGADA VÁLIDA")
        jogada1(a1,pos1,matriz,d)
        resultado(matriz)
        teste(matriz,z)
        if z == 1:
            pont1+=1
            break
            
        elif ctr%2==0:
            if ctr%2!=0:
                while True:
                    d = 0
                    pos1 = str(input("DIGITE SUA JOGADA JOGADOR 2: "))
                    jogada1(a2,pos1,matriz,d)
                    if d != 0:
                        break
                    else:
                        print("DIGITE UMA JOGADA VÁLIDA")
            jogada1(a2,pos1,matriz,d)
            resultado(matriz)
            teste(matriz,z)
            if z == 1:
                pont1+=1
                break

        ctr+=1
    if z == 0:
        print("EMPATE!")
    placar(pont1,pont2)
    break