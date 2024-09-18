import os

segredo = "avenida"
segredo_atual = '*' * len(segredo)
segredo_atual_list = list(segredo_atual)
tentativas = 5

def testar_letra(letra):
    global segredo_atual
    for index, char in enumerate(segredo):
        if char == letra:
            segredo_atual_list[index] = letra
    segredo_atual = "".join(segredo_atual_list)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{tentativas} tentativas restantes.")
    print(f"{segredo_atual}")

print(f"A palavra é: {segredo_atual}")
while tentativas > 0:
    letra = input("LETRA: ").lower()
    
    if letra in segredo:
        testar_letra(letra)
        
        # Verifica se a palavra foi completamente descoberta
        if segredo_atual == segredo:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Parabéns! Você descobriu a palavra: {segredo}")
            break
        
    else:
        tentativas -= 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("A palavra não possui essa letra!!")
        print(f"{tentativas} tentativas restantes.")
        segredo_atual = "".join(segredo_atual_list)
        print(f"{segredo_atual}")
else:
    if segredo_atual != segredo:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Acabaram suas tentativas! A palavra era:", segredo)
