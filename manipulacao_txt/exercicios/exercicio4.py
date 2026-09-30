def contar_linhas(nome_arquivo):
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print(f"O arquivo possui {len(linhas)} linhas.")


# Teste:
contar_linhas("nomes.txt")