def contar_caracteres():
    with open("texto.txt", "r") as arquivo:
        texto = arquivo.read()

    quantidade = len(texto)

    print("Quantidade de caracteres:", quantidade)


contar_caracteres()
