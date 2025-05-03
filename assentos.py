# estetica
def pause(): input("  (enter) ")

# funcao para ocupar o assento escolhido pelo passageiro
def registrar(matrizAssentos, posicao, row, valueRow):
    # verificando se a posicao recebida esta vazia
    if matrizAssentos[row][posicao-valueRow] == 0: # se o resultado for 0 = livre, se for 1 = ocupado
        decisao = str(input("\nTem certeza que deseja ocupar esse assento: (s/n) "))
        if decisao == "s":
            # alterando o assento na posicao especifica, de livre (0) para ocupado (1)
            matrizAssentos[row][posicao-valueRow] = 1 
        else:
            # caso o passageiro esolha "nao"
            return "assento nao reservado"  
    else:
        # caso a posicao escolhida for = 1
        print("\nEste assento já está ocupado!\n")
        pause()
        # retorno que sera tratado no main.py
        return "assento nao reservado"  

# funcao que ira receber o valor do assento do passageiro
def ocupar_assento(matriz_assentos):
    # recebendo valor do assento
    posicao_assento = int(input("\nDigite o numero do assento de 1-12: "))

    # verificando posicao
    if posicao_assento == 1 or posicao_assento == 2:
        # enviando a posicao para a funcao registrar,
        # para ser verificada se a posicao esta vazia ou nao
        return registrar(matriz_assentos, posicao_assento, 0, 1) # (Matriz de assentos / N° da posicao / linha / coluna)
        
    elif posicao_assento == 3 or posicao_assento == 4:
        return registrar(matriz_assentos, posicao_assento, 1, 3)

    elif posicao_assento == 5 or posicao_assento == 6:
        return registrar(matriz_assentos, posicao_assento, 2, 5)

    elif posicao_assento == 7 or posicao_assento == 8:
        return registrar(matriz_assentos, posicao_assento, 3, 7)

    elif posicao_assento == 9 or posicao_assento == 10:
        return registrar(matriz_assentos, posicao_assento, 4, 9)

    elif posicao_assento == 11 or posicao_assento == 12:
        return registrar(matriz_assentos, posicao_assento, 5, 11)

    else:
        # caso o passageiro nao escolha um valor valido
        print("\nEscolha um valor valido de 1-12!\n")
        pause()
        # retorno que sera tratado no main.py
        return "assento nao reservado"  