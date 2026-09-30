def calcular_estoque(nome_arquivo):
  valor_total = 0.0
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(";")
      preco = float(dados[1])
      quantidade = int(dados[2])
      valor_total += preco * quantidade

  print(f"Valor total do estoque: R$ {valor_total:.2f}")



calcular_estoque("produtos.txt")