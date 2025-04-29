def registrar(matrizAssentos, posicao, column, row):
    if matrizAssentos[column][posicao-row] == 0: # setando assento
        decisao = str(input("Tem certeza que deseja ocupar esse assento: (s/n) "))
        print()
        if decisao == "s":
            matrizAssentos[column][posicao-row] = 1 
        else:
            return "assento nao reservado"  
    else:
        print()
        print("Este assento já está ocupado!\n")
        return "assento nao reservado"  

def ocupar_assento(matriz_assentos):
    posicao = int(input("\nDigite o numero do assento: "))

    if posicao == 1 or posicao == 2:
        return registrar(matriz_assentos, posicao, 0, 1)
        
    elif posicao == 3 or posicao == 4:
        return registrar(matriz_assentos, posicao, 1, 3)

    elif posicao == 5 or posicao == 6:
        return registrar(matriz_assentos, posicao, 2, 5)

    elif posicao == 7 or posicao == 8:
        return registrar(matriz_assentos, posicao, 3, 7)

    elif posicao == 9 or posicao == 10:
        return registrar(matriz_assentos, posicao, 4, 9)

    elif posicao == 11 or posicao == 12:
        return registrar(matriz_assentos, posicao, 5, 11)

    else:
        print("\nEscolha outro valor!\n")
        return "assento nao reservado"  