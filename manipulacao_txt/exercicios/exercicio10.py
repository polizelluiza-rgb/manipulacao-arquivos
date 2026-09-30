def separar_numeros(nome_arquivo):
  pares = []
  impares = []
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      numero = int(linha.strip())
      if numero % 2 == 0:
        pares.append(numero)
      else:
        impares.append(numero)

  print("Números pares:")
  print(pares)
  print("\nNúmeros ímpares:")
  print(impares)



separar_numeros("numeros.txt")