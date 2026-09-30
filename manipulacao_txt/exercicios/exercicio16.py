def buscar_produto(nome_arquivo):
  produtos = []
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(";")
      produtos.append({
          "nome": dados[0],
          "preco": float(dados[1]),
          "quantidade": int(dados[2]),
      })

  pesquisa = input("Digite o produto: ")
  encontrado = None
  for p in produtos:
    if p["nome"].lower() == pesquisa.lower():
      encontrado = p
      break

  if encontrado:
    print("\nProduto encontrado!")
    print(f"Nome: {encontrado['nome']}")
    print(f"Preço: R$ {encontrado['preco']:.2f}")
    print(f"Quantidade: {encontrado['quantidade']}")
  else:
    print("\nProduto não encontrado!")



buscar_produto("produtos.txt")