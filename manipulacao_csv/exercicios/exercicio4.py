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
    print("\n===== GERADOR DE ARQUIVOS =====")
    print("1 - Listar treinadores")
    print("2 - Gerar CSV de um treinador")
    print("3 - Gerar CSV de todos os Pokémon (ordenados)")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print("\n--- Treinadores ---")
      for t in treinadores:
        print(f"- {t['nome']}")

    elif opcao == "2":
      nome = input("Digite o nome do treinador: ").strip()
      p_treinador = [
          p for p in pokemons if p["treinador"].lower() == nome.lower()
      ]

      if not p_treinador:
        print("Nenhum Pokémon encontrado para este treinador.")
        continue

      nome_arquivo = f"pokemons_{'_'.join(nome.lower().split())}.csv"
      campos = ["nome", "tipo", "nivel", "treinador"]

      with open(
          nome_arquivo, mode="w", newline="", encoding="utf-8"
      ) as arquivo_out:
        escritor = csv.DictWriter(arquivo_out, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(p_treinador)

      print(
          f"\nArquivo '{nome_arquivo}' gerado com sucesso!"
          f" {len(p_treinador)} registros gravados."
      )

    elif opcao == "3":
      pokemons_ordenados = sorted(
          pokemons, key=lambda x: int(x["nivel"]), reverse=True
      )
      nome_arquivo = "todos_pokemons_ordenados.csv"
      campos = ["nome", "tipo", "nivel", "treinador"]

      with open(
          nome_arquivo, mode="w", newline="", encoding="utf-8"
      ) as arquivo_out:
        escritor = csv.DictWriter(arquivo_out, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(pokemons_ordenados)

      print(
          f"\nArquivo '{nome_arquivo}' gerado com sucesso!"
          f" {len(pokemons_ordenados)} registros gravados."
      )

    elif opcao == "4":
      print("Programa encerrado.")
      break
    else:
      print("Opção inválida.")


menu()