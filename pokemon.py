import os
os.system('cls')


tipos = [
    "Normal", "Fogo", "Água", "Grama", "Elétrico", "Gelo", "Lutador", "Venenoso",
    "Terra", "Voador", "Psíquico", "Inseto", "Pedra", "Fantasma", "Dragão", 
    "Sombrio", "Aço", "Fada"
    ]

fraquezas = [ 
    ["Lutador"],           # Fraquezas de Normal
    ["Água", "Terra", "Pedra"],  # Fraquezas de Fogo
    ["Elétrico", "Grama"],  # Fraquezas de Água
    ["Fogo", "Gelo", "Voador", "Inseto"],  # Fraquezas de Grama
    ["Terra"],              # Fraquezas de Elétrico
    ["Fogo", "Lutador", "Pedra", "Aço"],  # Fraquezas de Gelo
    ["Voador", "Psíquico", "Fada"],  # Fraquezas de Lutador
    ["Terra", "Psíquico"],   # Fraquezas de Venenoso
    ["Água", "Gelo", "Grama"],  # Fraquezas de Terra
    ["Elétrico", "Gelo", "Pedra"],  # Fraquezas de Voador
    ["Inseto", "Fantasma", "Sombrio"],  # Fraquezas de Psíquico
    ["Fogo", "Voador", "Pedra"],  # Fraquezas de Inseto
    ["Água", "Grama", "Lutador", "Terra", "Aço"],  # Fraquezas de Pedra
    ["Fantasma", "Sombrio"],  # Fraquezas de Fantasma
    ["Gelo", "Dragão", "Fada"],  # Fraquezas de Dragão
    ["Lutador", "Inseto", "Fada"],  # Fraquezas de Sombrio
    ["Fogo", "Lutador", "Terra"],  # Fraquezas de Aço
    ["Veneno", "Aço"] #Fraquezas de fada
    ]

fortitude = [ 
    ["Nenhum"],              # Fortitudes de Normal
    ["Grama", "Gelo", "Inseto", "Aço"],  # Fortitudes de Fogo
    ["Fogo", "Terra", "Pedra"],  # Fortitudes de Água
    ["Água", "Terra", "Pedra"],  # Fortitudes de Grama
    ["Água", "Voador"],       # Fortitudes de Elétrico
    ["Grama", "Terra", "Voador", "Dragão"],  # Fortitudes de Gelo
    ["Normal", "Gelo", "Pedra", "Aço"],  # Fortitudes de Lutador
    ["Grama", "Fada"],        # Fortitudes de Venenoso
    ["Fogo", "Elétrico", "Venenoso", "Pedra", "Aço"],  # Fortitudes de Terra
    ["Grama", "Lutador", "Inseto"],  # Fortitudes de Voador
    ["Lutador", "Venenoso"],  # Fortitudes de Psíquico
    ["Grama", "Psíquico", "Sombrio"],  # Fortitudes de Inseto
    ["Fogo", "Gelo", "Voador", "Inseto"],  # Fortitudes de Pedra
    ["Psíquico", "Fantasma"],  # Fortitudes de Fantasma
    ["Dragão"],              # Fortitudes de Dragão
    ["Psíquico", "Fantasma"],  # Fortitudes de Sombrio
    ["Gelo", "Pedra", "Fada"],  # Fortitudes de Aço
    ["Lutador", "Dragão", "Sombrio"]  # Fortitudes de Fada
    ]


print("Por favor, usar apenas os números indicados na tabela.")
print("Caso o pokemon não tenha 2 tipos, apenas coloque 'n' ")
print("Para sair, digite 'SAIR'.")

while True:
    print("Lista de tipos: ")
    for i, tipo in enumerate(tipos):
        print(f"{i+1}º {tipo}")

    tipo1 = str(input("Digite o primeiro tipo do pokémon: "))
    if tipo1 == 'sair':
        print("Programa encerrado.")
        break
    tipo2 = str(input("Digite o Segundo tipo do pokémon: "))
    if tipo2 == 'sair':
        print("Programa encerrado.")
        break

    if tipo1.isdigit() and tipo2.isdigit():
        tipo1 = int(tipo1) - 1  
        tipo2 = int(tipo2) - 1 
    
        if 0 <= tipo1 < len(tipos) and 0 <= tipo2 < len(tipos):
            fraquezas_tipo1 = set(fraquezas[tipo1])
            fraquezas_tipo2 = set(fraquezas[tipo2])
            fortitude_tipo1 = set(fortitude[tipo1])
            fortitude_tipo2 = set(fortitude[tipo2])

            fraquezas_juntas = (fraquezas_tipo1 | fraquezas_tipo2) - (fortitude_tipo1|fortitude_tipo2)
            fortitude_juntas = (fortitude_tipo1|fortitude_tipo2)
            print(f"\nTipo 1: {tipos[tipo1]}, tipo 2: {tipos[tipo2]}")
            print(f"Fraquezas: {', '.join(fraquezas_juntas)}")
            print(f"Fortitudes: {', '.join(fortitude_juntas)}")
        else:
            print("Tipo inválido.")
