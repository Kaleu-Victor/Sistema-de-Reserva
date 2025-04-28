
assentos = [["L","O","L"],["O","O","L"],["L","L","O"]]
cadeiras = [["1","2","3"],["4","5","6"],["7","8","9"]]

print("Assentos do Avião:")
for i in cadeiras:
    for o in i:
        print(f"{o} - ", end="")

while True:
    print()
    print()
    for i in assentos:
        print(i)
    print()
    posicao = int(input("Digite o numero do assento: "))

    if posicao >= 1 and posicao <= 3:
        print(assentos[0][posicao-1]) # pegando assentos
        if assentos[0][posicao-1] == "L": # setando assento
            decisao = str(input("Tem certeza que quer comprar essa vaga? (s/n) "))
            if decisao == "s":
                assentos[0][posicao-1] = "O"
        else:
            print()
            print("Este assento já está ocupado!")
    if posicao >= 4 and posicao <= 6:
        if assentos[1][posicao-4] == "L":
            decisao = str(input("Tem certeza que quer comprar essa vaga? (s/n) "))
            if decisao == "s":
                assentos[1][posicao-4] = "O"
        else:
            print()
            print("Este assento já está ocupado!")

    if posicao >= 7 and posicao <= 9:
        if assentos[2][posicao-7] == "L":
            decisao = str(input("Tem certeza que quer comprar essa vaga? (s/n) "))
            if decisao == "s":
                assentos[2][posicao-7] = "O"
        else:
            print()
            print("Este assento já está ocupado!")

