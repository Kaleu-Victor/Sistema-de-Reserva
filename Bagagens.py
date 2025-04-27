bagagens = []

while True:
    print("======================")
    print("1. Adicionar bagagem")
    print("2. Listar bagagens")
    print("3. Remover bagagem")
    print("4. Sair")
    print("======================")

    op = int(input("Selecione uma das opções de 1 a 4: "))

    if op == 1:
        num_bagagem = int(input("Número da bagagem: "))
        peso_bagagem = float(input("Peso da bagagem (kg): "))
        destino_bagagem = str(input("Destino da bagagem: "))

        bagagem = [num_bagagem, peso_bagagem, destino_bagagem]

        bagagens.append(bagagem)
    
    if op == 2:
        for bagagem in bagagens:
            print(f"Número da bagagem: {bagagem[0]} | Peso: {bagagem[1]}kg | Destino: {bagagem[2]} ")

    if op == 3:
        remover_ultima_bagagem = bagagem.remove()

    if op == 4:
        print("Sistema encerrado.")
        break