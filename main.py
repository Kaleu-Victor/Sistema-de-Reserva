import numpy as np
import assentos as ast
import bagagens as bgg

# Criação e inicialização das matrizes
assentos_ex = np.zeros([6,2])
assentos_ec = np.zeros([6,2])
estoque_malas = np.zeros([7,7]) # 7,7 

def pause(): input("  (enter) ")

while True:
    # Exibindo as matrizes
    print(f"Assentos classe Executiva:\n{assentos_ex}")
    print("=====================\n")

    print(f"Assentos classe Econômica:\n{assentos_ec}")
    print("=====================\n")

    print(f"Estoque de Bagagens:\n{estoque_malas}\n")
    print("\n----------------------------------------")

    decisao = str(input("Quer reservar um assento no Aviao: (s/n) "))

    if decisao == "s":
        classe = str(input("\nClasse Excutiva (R$ 3.500,00) ou Economica (R$ 1.150,00): (ex/ec) "))

        def cauloValorpassagem(cad, mala, valor_bagagen):
            precoTotal = cad + (mala * valor_bagagen)            
            print("\n--------------------------------------------")
            print(f"° Valor da passagem: R$ {cad},00.")
            print(f"° Valor da bagagem (R$ {valor_bagagen},00): R$ {malas * valor_bagagen},00.")
            print(f"° TOTAL A PAGAR: R$ {precoTotal},00.")
            print("--------------------------------------------\n")
            pause()
        
        if classe == "ex":
            cadeira = 3500
            valor_das_bagagens = 400
            decisao = ast.ocupar_assento(assentos_ex)

            if decisao != "assento nao reservado": 
                if estoque_malas[6][6] == 1: # 6,6
                    print("\n ATENCAO!\n Nao e mais possivel adicionar bagagens!\n")
                else:   
                    malas = bgg.bagagem(estoque_malas, classe)
                    cauloValorpassagem(cadeira, malas, valor_das_bagagens)

        elif classe == "ec":
            cadeira = 1150
            valor_das_bagagens = 200
            decisao = ast.ocupar_assento(assentos_ec) 

            if decisao != "assento nao reservado": 
                if estoque_malas[6][6] == 1: # 6,6
                    print("\n ATENCAO!\n Nao e mais possivel adicionar bagagens!\n")
                else:   
                    malas = bgg.bagagem(estoque_malas, classe)
                    cauloValorpassagem(cadeira, malas, valor_das_bagagens)

        else:
            print("\n É complicado né!\n")
            pause()
    else:
        print("\n É complicado né!\n")
        pause()