def gerar_relatorio(nome_arquivo):
  total_geral = 0.0
  vendas_por_vendedor = {}

  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(";")
      vendedor, produto, valor = dados[0], dados[1], float(dados[2])
      total_geral += valor

      if vendedor in vendas_por_vendedor:
        vendas_por_vendedor[vendedor] += 1
      else:
        vendas_por_vendedor[vendedor] = 1

  print(f"TOTAL DE VENDAS: R$ {total_geral:.2f}\n")
  print("Quantidade de vendas:")
  for v, qtd in vendas_por_vendedor.items():
    print(f"{v}: {qtd}")



gerar_relatorio("vendas.txt")