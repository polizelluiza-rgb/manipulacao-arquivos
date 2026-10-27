import csv


def ler_dados(nome_arquivo):
  lista = []
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
      lista.append(linha)
  return lista


def menu():
  treinadores = ler_dados("treinadores.csv")
  pokemons = ler_dados("pokemons.csv")

  while True:
    print("\n===== RELATÓRIOS =====")
    print("1 - Relatório de um treinador")
    print("2 - Média de nível dos Pokémon de um treinador")
    print("3 - Média de nível dos Pokémon por tipo")
    print("4 - Quantidade de Pokémon por treinador")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      nome = input("Digite o nome do treinador: ").lower()
      t_encontrado = next(
          (t for t in treinadores if t["nome"].lower() == nome), None
      )

      if not t_encontrado:
        print("Treinador não encontrado.")
        continue

      print(f"\nTreinador: {t_encontrado['nome']}")
      print(f"Região: {t_encontrado['regiao']}")
      print(f"Nível: {t_encontrado['nivel']}\n")
      print("Pokémon:")

      for p in pokemons:
        if p["treinador"].lower() == nome:
          print(f"- {p['nome']} - {p['tipo']} - Nível {p['nivel']}")

    elif opcao == "2":
      nome = input("Digite o nome do treinador: ").lower()
      p_treinador = [p for p in pokemons if p["treinador"].lower() == nome]

      if not p_treinador:
        print("Nenhum Pokémon encontrado.")
        continue

      soma = sum(int(p["nivel"]) for p in p_treinador)
      media = soma / len(p_treinador)
      print(f"Média de nível dos Pokémon: {media:.2f}")

    elif opcao == "3":
      tipo = input("Digite o tipo de Pokémon: ").lower()
      p_tipo = [p for p in pokemons if p["tipo"].lower() == tipo]

      if not p_tipo:
        print("Nenhum Pokémon desse tipo encontrado.")
        continue

      soma = sum(int(p["nivel"]) for p in p_tipo)
      media = soma / len(p_tipo)
      print(f"Média de nível do tipo {tipo}: {media:.2f}")

    elif opcao == "4":
      contagem = {}
      for p in pokemons:
        t = p["treinador"]
        contagem[t] = contagem.get(t, 0) + 1

      print("\nQuantidade de Pokémon por treinador:")
      for t, qtd in contagem.items():
        print(f"- {t}: {qtd} Pokémon")

    elif opcao == "5":
      print("Encerrando relatórios.")
      break
    else:
      print("Opção inválida.")


menu()