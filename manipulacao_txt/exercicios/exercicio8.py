def contar_palavras(nome_arquivo):
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    print(f"Quantidade de palavras: {len(palavras)}")



contar_palavras("arquivo texto.txt")