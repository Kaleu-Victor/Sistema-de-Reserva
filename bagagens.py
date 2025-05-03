# estetica
def pause(): input("  (enter) ")

# funcao para armazenar as bagagens
def bagagem(matriz_bagagens, classe): # (Matriz bagagens / "Executiva" ou "Econonica")
    decisao = str(input("\nVoce tem bagagem: (s/n) "))

    # mostrando valor da bagens por unidade a depender da classe
    if classe == "ex": print("° Classe Executiva: R$ 400,00 (por bagagem)")
    else: print("° Classe Economica: R$ 200,00 (por bagagem)")


    if decisao == "s":
        bagagensParaAdicionar = 0 # N° de baganges validas 
        espaco_ocupado_na_matriz = 0 # N° de espaços ocupados na matriz bagagens

        # percorrendo a matriz bagagens
        for i_ in matriz_bagagens:
            for o_ in i_:
                # verificando se este espaço esta ocupado
                if o_ == 1:
                    # encrementando valor de espaço ocupado na variavel
                    espaco_ocupado_na_matriz += 1
                # assim que encontrar o primeiro valor 0 o loop vai ser encerrado
                else: break 
        
        # obtendo valor de malas do passageiro
        qtd_malas = int(input(f"\nQuantas malas: (limite {49 - espaco_ocupado_na_matriz}) ")) # limite = (espaço da matriz - epaço ja ocupado na matriz)
        
        # verificando se a quantidade de malas é menor ou igual ao valor limite
        if qtd_malas >= 1 and qtd_malas <= (49 - espaco_ocupado_na_matriz):
            
            # loop mediante o numero de malas 
            for i in range(1, qtd_malas+1):
                
                # funçao de erro ao adicionar uma mala por limite de peso
                def erroAoAdicionar():
                    print("\n!! ATENCAO !!")
                    print(f"Esta mala ultrapassa os limites de peso, portanto nao sera armazenada.\n")
                    print("OPCOES:")
                    print("1 - Continuar adicionando a proxima mala")
                    print("2 - Parar")
                    decisaoDoPassageiro = int(input("> "))
                    if decisaoDoPassageiro == 2:
                        print("\n- As malas (registradas com sucesso) foram armazenadas!")
                        # retorno caso o passageiro decida parar de adicinar malas
                        return "parar"
                    # caso nao pare, ele ira continuar adicionando baganges se tiver
                    else: pass

                print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                peso_mala = float(input(f"Digite o peso(kg) da mala {i}: ")) # obtendo peso da mala  
                
                
                if classe == "ex":
                    # verificando peso da mala mediante a classe
                    if peso_mala <= 32: bagagensParaAdicionar += 1
                    # se o peso passar do limite, a funcao erroAoAdicionar sera chamada
                    else: 
                        # ao chamar a funcao erroAoAdicionar se ela retorar "parar" o loop de adicionar malas sera parado
                        if erroAoAdicionar() == "parar": break

                elif classe == "ec": 
                    # verificando peso da mala mediante a classe
                    if peso_mala <= 23: 
                        bagagensParaAdicionar += 1 # caso o valor seja menor ou igual ao limite 
                    # da classe economica (23), +1 sera adicionado na variavel bagagensParaAdicionar
                    else:
                        if erroAoAdicionar() == "parar": break

            # varivel contendo o valor total de malas validas para serem armazenadas
            _bagagensSalvas = bagagensParaAdicionar

            # funcao que ira armazenar as malas
            def verificar(numero_de_malas): # recebendo numero de malas
                global espaco_vazio_encontrado # variavel global
                espaco_vazio_encontrado = 0 # sera acesada para verificar a existencia de espaços livres na matriz bagagem

                # iterando sobre a matriz bagagens 7x7
                for i_ in range(0, 7): 
                    for o_ in range(0, 7):
                        # verificando se a posicao obtida na matriz é igual a 0 = livre
                        if matriz_bagagens[i_][o_] == 0: 
                            numero_de_malas -= 1 # decrementando valor, indicando que a mala foi armazenada na matriz
                            espaco_vazio_encontrado = 1 # declarando que um espaço vazio foi encontrado
                            matriz_bagagens[i_][o_] = 1 # armazenando mala
                            break # parando o loop
                        else:pass

                    # verificando se o espaço livre foi encontrado
                    if espaco_vazio_encontrado == 0: pass
                    else: 
                        break # caso encontrado o loop vai parar
                
                # retorando o n° de malas armazenadas
                return numero_de_malas
            
            # verificando se existe alguma mala valida para armazenar
            if bagagensParaAdicionar >= 1:
                # iterando pela quantidade de malas validas 
                for i in range(1, bagagensParaAdicionar+1):
                    # chamando a funcao que ira armazenar a mala
                    bagagensParaAdicionar = verificar(bagagensParaAdicionar) # essa funcao vai retornar um valor, que 
                    # sera decrementado na variavel bagagensParaAdicionar

            # retornrando valor total de malas armazenadas
            return _bagagensSalvas
        else:
            # caso o passageiro escolha tenha mais malas que o limite na matriz
            print("\nNão é possivel armazenar a bagagem!")
            pause()
            _bagagensSalvas = 0 # nenhuma mala foi salva, logo _bagagensSalvas deve ser 0
            return _bagagensSalvas # retornando valor de malas armazenadas
        
    # caso o passageiro nao tenha malas para guardar
    else:
        _bagagensSalvas = 0
        return _bagagensSalvas # retornando valor de malas armazenadas