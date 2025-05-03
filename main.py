import numpy as np
import assentos as ast
import bagagens as bgg

# criação e inicialização das matrizes com 0
assentos_ex = np.zeros([6,2])
assentos_ec = np.zeros([6,2])
estoque_malas = np.zeros([7,7]) # 7,7 

# funcao para estética na tela
def pause(): input("  (enter) ")

while True:
    # exibindo as matrizes
    print(f"Assentos classe Executiva:\n{assentos_ex}")
    print("=====================\n")

    print(f"Assentos classe Econômica:\n{assentos_ec}")
    print("=====================\n")

    print(f"Estoque de Bagagens:\n{estoque_malas}\n")
    print("\n----------------------------------------")

    decisao = str(input("Quer reservar um assento no Aviao: (s/n) "))

    # obtendo o valor da variavel em minusculo
    if decisao.lower() == "s":
        # obtendo a classe que o passageiro deseja ir
        classe = str(input("\nClasse Excutiva (R$ 3.500,00) ou Economica (R$ 1.150,00): (ex/ec) "))

        # calculo de quanto o passageiro ira pagar
        def cauloValorpassagem(cad, mala, valorBagagen): # (Cadeira / Malas Armazenadas / Valor da Bagagem)
            precoTotal = cad + (mala * valorBagagen) # valor total a ser pago        
            print("\n--------------------------------------------")
            print(f"° Valor da passagem: R$ {cad},00.")
            print(f"° Valor da bagagem (R$ {valorBagagen},00): R$ {mala * valorBagagen},00.")
            print(f"° TOTAL A PAGAR: R$ {precoTotal},00.")
            print("--------------------------------------------\n")
            pause()
        
        # verificando a classe
        if classe == "ex":
            cadeira = 3500 # setando o valor da cadeira 
            valor_das_bagagens = 400 # setando o valor das bagagens (por unidade)
            # funcao para ocupar um assento na matriz
            decisao_assento_ex = ast.ocupar_assento(assentos_ex) # vai retornar uma string se o passageiro ocupou ou nao o assento

            if decisao_assento_ex != "assento nao reservado": # verificando o valor da variavel recebida na funcao de assentos
                # verificando se a matriz bagagens esta cheia
                if estoque_malas[6][6] == 1: # 6,6
                    print("\n!! ATENCAO !!\n Nao e mais possivel adicionar bagagens!\n")
                    pause()
                else:   
                    # funcao para armazenar bagagens
                    malas_salvas_ex = bgg.bagagem(estoque_malas, classe) # vai retornar um numero de quantas malas foram armazenadas
                    # funcao para calcular o preco a ser pago pelo passageiro
                    cauloValorpassagem(cadeira, malas_salvas_ex, valor_das_bagagens) # (Preco do assento / N° de malas armazenadas / Valor da bagagem )

        elif classe == "ec":
            cadeira = 1150
            valor_das_bagagens = 200
            decisao_assento_ec = ast.ocupar_assento(assentos_ec) 

            if decisao_assento_ec != "assento nao reservado": 
                if estoque_malas[6][6] == 1:
                    print("\n!! ATENCAO !!\nNao e mais possivel adicionar bagagens!\n")
                    pause()
                else:   
                    malas_salvas_ec = bgg.bagagem(estoque_malas, classe)
                    cauloValorpassagem(cadeira, malas_salvas_ec, valor_das_bagagens)

        # se o passageiro nao escolheu a classe corretamente
        else:
            print("\n- É complicado né!\n")
            pause()
    # se o passageiro nao quer continuar o programa
    else: 
        # verificando se ele quer sair
        decisao = input("\nSair do programa: (s/n) ")
        if decisao.lower() == "s": 
            print("\nPrograma encerrado!\n")
            quit() # encerrando o programa