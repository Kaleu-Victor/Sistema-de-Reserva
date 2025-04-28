# ['L', 'L', 'L']
# ['L', 'L', 'L']
# ['L', 'L', 'L']

matriz_bagagens = [["*","*","*"],["*","*","*"],["*","*","*"]]

def overheadBin():pass

def porao():pass

def baguagem():
    print()
    print("BAGAGENS:")
    for inn in matriz_bagagens:
        print(inn)
    print()
    decisao = str(input("Voce tem bagagem: (s/n) "))

    if decisao == "s":
        classe = str(input("Classe Excutiva ou Economica: (ex/ec) "))
        bagagensParaAdicionar = 0
        qtd = int(input("Quantas malas: "))
        for i in range(1, qtd+1):
            print("#########################################")
            peso = float(input(f"Digite o peso da mala {i}: "))
            comprimento = float(input("Dimensoes da bagagem (comprimento): "))
            largura = float(input("Dimensoes da bagagem (largura): "))
            altura = float(input("Dimensoes da bagagem (altura): "))
            print() 

            def erroAoAdicionar(erro):
                print("!! ATENCAO !!")
                print(f"Esta mala ultrapassa os limites de {erro}.")
                print()
                print("OPCOES:")
                print("1 - Continuar adicionando a proxima mala")
                print("2 - Parar")
                decisao = int(input("> "))
                print()
                if decisao == 2:
                    print("! As malas (registradas com sucesso) serao guardadas!")
                    print()
                    return "parar"
                else: pass

            if classe == "ex":
                if peso <= 16: # 14
                    if comprimento <= 55 and largura <= 35 and altura <= 25: # verificando tamanho da baguagem
                        bagagensParaAdicionar += 1
                    else:
                        if erroAoAdicionar("dimensoes aceitas") == "parar": break
                else:
                    if erroAoAdicionar("peso") == "parar": break

            elif classe == "ec":
                if peso <= 9.5:
                    if comprimento <= 55 and largura <= 35 and altura <= 25:
                        bagagensParaAdicionar += 1
                    else:
                        if erroAoAdicionar("dimensoes aceitas") == "parar": break
                else:
                    if erroAoAdicionar("peso") == "parar": break
        
        def verificar(bbb):
            global achou
            achou = 0
            for i_ in range(0, 3):
                for o_ in range(0, 3):
                    if matriz_bagagens[i_][o_] == "*":
                        bbb -= 1
                        achou = 1
                        matriz_bagagens[i_][o_] = "#"
                        break
                    else:pass
                if achou == 0: pass
                else: 
                    break
            return bbb
        
        if bagagensParaAdicionar >= 1:
            for i in range(1, bagagensParaAdicionar+1):
                bagagensParaAdicionar = verificar(bagagensParaAdicionar)
            
    else:
        print()
        print("Programa encerrado!")
        print()
        quit()
while True:
    baguagem()