def cadastrar_produtos(nome_arquivo):
  produtos = []
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(";")
      produto = {
          "nome": dados[0],
          "preco": float(dados[1]),
          "quantidade": int(dados[2]),
      }
      produtos.append(produto)
  return produtos



print(cadastrar_produtos("produtos.txt"))