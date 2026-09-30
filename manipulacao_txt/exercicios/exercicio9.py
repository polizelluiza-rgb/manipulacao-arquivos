def mostrar_numeros(nome_arquivo):
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      numero = int(linha.strip())
      if numero % 2 == 0:
        print(numero)



mostrar_numeros("numeros.txt")