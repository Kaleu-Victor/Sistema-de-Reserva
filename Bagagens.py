import numpy as np

# Adição das matrizes
assentos_ex = np.zeros([6,2])
assentos_ec = np.zeros([6,2])
estoque_malas = np.zeros([7,7])

assentos_ex[0][0] = 1
assentos_ex[2][0] = 1
assentos_ex[4][0] = 1
assentos_ex[1][1] = 1
assentos_ex[2][1] = 1
assentos_ex[3][1] = 1
assentos_ex[5][1] = 1

assentos_ec[0][0] = 1
assentos_ec[0][1] = 1
assentos_ec[3][0] = 1
assentos_ec[3][1] = 1
assentos_ec[5][0] = 1
assentos_ec[5][1] = 1

print(f"\nAssentos Executivos:\n{assentos_ex}")
print("\n=====================\n")
print(f"\nAssentos Econômicos:\n{assentos_ec}")
print("\n=====================\n")
print(f"Estoque de Bagagens:\n{estoque_malas}\n")


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
        if not bagagens:
            print("Nenhuma bagagem cadastrada")
        else:
            for bagagem in bagagens:
                print(f"Número da bagagem: {bagagem[0]} | Peso: {bagagem[1]}kg | Destino: {bagagem[2]} ")

    if op == 3:
        del_bagagem = int(input("Qual é o número da bagagem para ser removida? "))
        encontrado = False
        for bagagem in bagagens:
            if bagagem[0] == del_bagagem:
                bagagens.remove(bagagem)
                print(f"Bagagem | {del_bagagem} | removida com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print(f"Bagagem número | {del_bagagem} | não encontrada.")

    if op == 4:
        print("Sistema encerrado.")
        break
