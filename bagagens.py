def pause(): input("  (enter) ")

def bagagem(matriz_bagagens, classe):
    decisao = str(input("\nVoce tem bagagem: (s/n) "))

    if decisao == "s":
        bagagensParaAdicionar = 0
        espaco_ocupado_na_matriz = 0
        for i_ in matriz_bagagens:
            for o_ in i_:
                if o_ == 1:
                    espaco_ocupado_na_matriz += 1
                else: break

        qtd = int(input(f"\nQuantas malas: (limite {49 - espaco_ocupado_na_matriz}) ")) # 49
        if qtd >= 1 and qtd <= (49 - espaco_ocupado_na_matriz): # 49
            for i in range(1, qtd+1):
                def erroAoAdicionar():
                    print("\n!! ATENCAO !!")
                    print(f"Esta mala ultrapassa os limites de peso, portanto nao sera armazenada.\n")
                    print("OPCOES:")
                    print("1 - Continuar adicionando a proxima mala")
                    print("2 - Parar")
                    decisao = int(input("> "))
                    if decisao == 2:
                        print("\n- As malas (registradas com sucesso) foram armazenadas!")
                        return "parar"
                    else: pass

                print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                peso = float(input(f"Digite o peso(kg) da mala {i}: "))   
                
                if classe == "ex":
                    if peso <= 32: bagagensParaAdicionar += 1
                    else:
                        if erroAoAdicionar() == "parar": break

                elif classe == "ec":
                    if peso <= 23: bagagensParaAdicionar += 1
                    else:
                        if erroAoAdicionar() == "parar": break

            _bagagensSalvas = bagagensParaAdicionar

            def verificar(bbb):
                global achou
                achou = 0
                for i_ in range(0, 7): # 7
                    for o_ in range(0, 7):# 7
                        if matriz_bagagens[i_][o_] == 0:
                            bbb -= 1
                            achou = 1
                            matriz_bagagens[i_][o_] = 1
                            break
                        else:pass
                    if achou == 0: pass
                    else: 
                        break
                return bbb
           
            if bagagensParaAdicionar >= 1:
                for i in range(1, bagagensParaAdicionar+1):
                    bagagensParaAdicionar = verificar(bagagensParaAdicionar)

            return _bagagensSalvas
        else:
            print("\nNão é possivel armazenar a bagagem!")
            pause()
            _bagagensSalvas = 0
            return _bagagensSalvas
    else:
        _bagagensSalvas = 0
        return _bagagensSalvas 