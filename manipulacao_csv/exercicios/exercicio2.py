import csv


def criar_arquivos():

  with open("treinadores.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nome", "regiao", "nivel"])
    w.writerow(["Ash Ketchum", "Kanto", "90"])
    w.writerow(["Misty", "Kanto", "85"])


  with open("pokemons.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nome", "tipo", "nivel", "treinador"])
    w.writerow(["Pikachu", "Elétrico", "50", "Ash Ketchum"])
    w.writerow(["Metagross", "Fantasma", "41", "Ash Ketchum"])
    w.writerow(["Staryu", "Água", "35", "Misty"])


criar_arquivos()



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
    print("\n===== POKÉMON DOS TREINADORES =====")
    print("1 - Listar Pokémon de um treinador")
    print("2 - Contar Pokémon de um treinador")
    print("3 - Mostrar Pokémon de maior nível")
    print("4 - Mostrar Pokémon de menor nível")
    print("5 - Listar Pokémon de determinado tipo")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao in ["1", "2", "3", "4"]:
      nome = input("Digite o nome do treinador: ").lower()


      existe = any(t["nome"].lower() == nome for t in treinadores)
      if not existe:
        print("Treinador não encontrado.")
        continue


      p_treinador = [p for p in pokemons if p["treinador"].lower() == nome]

      if not p_treinador:
        print("Este treinador não possui Pokémon cadastrados.")
        continue

      if opcao == "1":
        print(f"\n--- Pokémon do treinador ---")
        for p in p_treinador:
          print(f"- {p['nome']} | Tipo: {p['tipo']} | Nível: {p['nivel']}")

      elif opcao == "2":
        print(f"Quantidade de Pokémon: {len(p_treinador)}")

      elif opcao == "3":
        maior = max(p_treinador, key=lambda x: int(x["nivel"]))
        print(
            "Pokémon de maior nível:"
            f" {maior['nome']} (Nível {maior['nivel']})"
        )

      elif opcao == "4":
        menor = min(p_treinador, key=lambda x: int(x["nivel"]))
        print(
            "Pokémon de menor nível:"
            f" {menor['nome']} (Nível {menor['nivel']})"
        )

    elif opcao == "5":
      tipo_busca = input("Digite o tipo (ex: Elétrico, Água): ").lower()
      encontrados = [p for p in pokemons if p["tipo"].lower() == tipo_busca]

      if encontrados:
        print(f"\n--- Pokémon do tipo {tipo_busca} ---")
        for p in encontrados:
          print(
              f"- {p['nome']} (Treinador: {p['treinador']} | Nível:"
              f" {p['nivel']})"
          )
      else:
        print("Nenhum Pokémon encontrado com esse tipo.")

    elif opcao == "6":
      print("Programa encerrado.")
      break
    else:
      print("Opção inválida.")


menu()