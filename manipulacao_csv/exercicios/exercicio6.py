import csv


def ler_dados(nome_arquivo):
  try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
      return list(csv.DictReader(arquivo))
  except FileNotFoundError:
    return []


def menu():
  treinadores = ler_dados("treinadores.csv")
  pokemons = ler_dados("pokemons.csv")
  classificacao_cache = []

  while True:
    print("\n===== CAMPEONATO POKÉMON =====")
    print("1 - Listar treinadores")
    print("2 - Consultar equipe")
    print("3 - Calcular pontuação")
    print("4 - Mostrar classificação")
    print("5 - Gerar arquivo CSV do campeonato")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print("\n--- Treinadores ---")
      for t in treinadores:
        print(f"- {t['nome']} (Região: {t['regiao']}, Nível: {t['nivel']})")

    elif opcao == "2":
      nome = input("Digite o nome do treinador: ").strip().lower()
      t_encontrado = None
      for t in treinadores:
        if t["nome"].lower() == nome:
          t_encontrado = t
          break

      if not t_encontrado:
        print("Treinador não encontrado.")
        continue

      print(f"\nTreinador: {t_encontrado['nome']}")
      print(f"Região: {t_encontrado['regiao']}")
      print(f"Nível: {t_encontrado['nivel']}\n")
      print("Pokémon da equipe:")

      p_equipe = [
          p for p in pokemons if p["treinador"].lower() == nome
      ]
      for i, p in enumerate(p_equipe, 1):
        print(f"{i} - {p['nome']} - {p['tipo']} - Nível {p['nivel']}")

    elif opcao == "3":
      classificacao_cache = []
      for t in treinadores:
        nome_t = t["nome"]
        p_treinador = [
            p for p in pokemons if p["treinador"].lower() == nome_t.lower()
        ]
        qtd_p = len(p_treinador)
        soma_niveis = sum(int(p["nivel"]) for p in p_treinador)
        pontuacao = int(t["nivel"]) + soma_niveis

        classificacao_cache.append({
            "treinador": nome_t,
            "regiao": t["regiao"],
            "nivel_treinador": int(t["nivel"]),
            "quantidade_pokemons": qtd_p,
            "soma_niveis": soma_niveis,
            "pontuacao": pontuacao,
        })
      print("\nPontuações calculadas com sucesso!")

    elif opcao == "4":
      if not classificacao_cache:
        print("Calcule a pontuação primeiro (Opção 3).")
        continue

      classificacao_ordenada = sorted(
          classificacao_cache, key=lambda x: x["pontuacao"], reverse=True
      )
      print("\n===== CLASSIFICAÇÃO =====")
      for i, c in enumerate(classificacao_ordenada, 1):
        print(
            f"{i}º Lugar: {c['treinador']} | Pontuação: {c['pontuacao']} pontos"
        )

    elif opcao == "5":
      if not classificacao_cache:
        print("Calcule a pontuação primeiro (Opção 3).")
        continue

      classificacao_ordenada = sorted(
          classificacao_cache, key=lambda x: x["pontuacao"], reverse=True
      )
      campos = [
          "treinador",
          "regiao",
          "nivel_treinador",
          "quantidade_pokemons",
          "soma_niveis",
          "pontuacao",
      ]

      with open(
          "resultado_campeonato.csv", "w", newline="", encoding="utf-8"
      ) as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(classificacao_ordenada)

      print(
          "Arquivo 'resultado_campeonato.csv' gerado com sucesso com"
          f" {len(classificacao_ordenada)} registros!"
      )

    elif opcao == "6":
      print("Programa encerrado.")
      break
    else:
      print("Opção inválida.")


menu()