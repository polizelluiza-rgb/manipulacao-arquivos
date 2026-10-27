import csv


def ler_pokemons():
  try:
    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
      return list(csv.DictReader(arquivo))
  except FileNotFoundError:
    return []


def menu():
  pokemons = ler_pokemons()

  while True:
    print("\n===== GERENCIADOR DE POKÉMON =====")
    print("1 - Listar Pokémon")
    print("2 - Pesquisar Pokémon")
    print("3 - Adicionar Pokémon")
    print("4 - Alterar nível de um Pokémon")
    print("5 - Remover Pokémon")
    print("6 - Salvar alterações")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print("\n--- Lista de Pokémon ---")
      for p in pokemons:
        print(
            f"Nome: {p['nome']} | Tipo: {p['tipo']} | Nível: {p['nivel']} |"
            f" Treinador: {p['treinador']}"
        )

    elif opcao == "2":
      nome = input("Digite o nome do Pokémon: ").strip().lower()
      encontrado = None
      for p in pokemons:
        if p["nome"].lower() == nome:
          encontrado = p
          break

      if encontrado:
        print(f"\nNome: {encontrado['nome']}")
        print(f"Tipo: {encontrado['tipo']}")
        print(f"Nível: {encontrado['nivel']}")
        print(f"Treinador: {encontrado['treinador']}")
      else:
        print("Pokémon não encontrado.")

    elif opcao == "3":
      nome = input("Nome: ").strip()
      tipo = input("Tipo: ").strip()
      nivel = input("Nível: ").strip()
      treinador = input("Treinador: ").strip()

      if not nome or not tipo or not nivel:
        print("Preencha todos os campos corretamente.")
        continue

      novo_pokemon = {
          "nome": nome,
          "tipo": tipo,
          "nivel": nivel,
          "treinador": treinador,
      }
      pokemons.append(novo_pokemon)
      print("Pokémon adicionado na lista com sucesso!")

    elif opcao == "4":
      nome = input("Digite o nome do Pokémon para alterar o nível: ").strip().lower()
      encontrado = False
      for p in pokemons:
        if p["nome"].lower() == nome:
          novo_nivel = input("Digite o novo nível: ").strip()
          p["nivel"] = novo_nivel
          print("Nível alterado com sucesso!")
          encontrado = True
          break
      if not encontrado:
        print("Pokémon não encontrado.")

    elif opcao == "5":
      nome = input("Digite o nome do Pokémon para remover: ").strip().lower()
      encontrado = False
      for p in pokemons:
        if p["nome"].lower() == nome:
          pokemons.remove(p)
          print("Pokémon removido com sucesso!")
          encontrado = True
          break
      if not encontrado:
        print("Pokémon não encontrado.")

    elif opcao == "6":
      campos = ["nome", "tipo", "nivel", "treinador"]
      with open(
          "pokemons_atualizados.csv", "w", newline="", encoding="utf-8"
      ) as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(pokemons)
      print("Alterações salvas em 'pokemons_atualizados.csv' com sucesso!")

    elif opcao == "7":
      print("Programa encerrado.")
      break
    else:
      print("Opção inválida.")


menu()