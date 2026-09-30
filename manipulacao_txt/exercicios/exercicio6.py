def carregar_nomes(nome_arquivo):
  nomes = []
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      nomes.append(linha.strip())
  print(nomes)
  return nomes



carregar_nomes("nomes.txt")