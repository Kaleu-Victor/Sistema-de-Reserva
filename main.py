import numpy as np
import assentos as ast
import bagagens as bgg

# Criação e inicialização das matrizes
assentos_ex = np.zeros([6,2])
assentos_ec = np.zeros([6,2])
estoque_malas = np.zeros([7,7]) # 7,7

while True:
    print(f"Assentos classe Executiva:\n{assentos_ex}")
    print("=====================\n")

    print(f"Assentos classe Econômica:\n{assentos_ec}")
    print("=====================\n")

    print(f"Estoque de Bagagens:\n{estoque_malas}\n")
    print("\n--------------------------\n")

    decisao = str(input("Voce gostaria reservar um assento no Aviao: (s/n) "))

    if decisao == "s":
        classe = str(input("Classe Excutiva ou Economica: (ex/ec) "))

        def passagem(cad, mala, valor_bagagen):
            precoTotal = cad + (mala * valor_bagagen)
            return precoTotal
        
        if classe == "ex":
            cadeira = 3500
            valor_das_bagagens = 400
            decisao = ast.ocupar_assento(assentos_ex)

            if decisao != "assento nao reservado": 
                if estoque_malas[6][6] == 1: # 6,6
                    print("\n ATENCAO!\n Nao e mais possivel adicionar bagagens!\n")
                else:   
                    malas = bgg.baguagem(estoque_malas, classe)
                    valor = passagem(cadeira, malas, valor_das_bagagens)
                    print("\n-------------------------------------")
                    print(f"TOTAL DA PASSAGEM: R$ {valor}.")
                    print("-------------------------------------\n")
        elif classe == "ec":
            cadeira = 1150
            valor_das_bagagens = 200
            decisao = ast.ocupar_assento(assentos_ec) 

            if decisao != "assento nao reservado": 
                if estoque_malas[6][6] == 1: # 6,6
                    print("\n ATENCAO!\n Nao e mais possivel adicionar bagagens!\n")
                else:   
                    malas = bgg.baguagem(estoque_malas, classe)
                    valor = passagem(cadeira, malas, valor_das_bagagens)
                    print("\n-------------------------------------")
                    print(f"TOTAL DA PASSAGEM: R$ {valor}.")
                    print("-------------------------------------\n")
        else:
            print("\n É complicado né!\n")
    else:
        print("\n É complicado né!\n")