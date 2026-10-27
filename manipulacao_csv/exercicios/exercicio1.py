import csv

def criar_arquivo_treinadores():
  treinadores_iniciais = [
      ["nome", "regiao", "nivel"],
      ["Ash Ketchum", "kanto", "90"],
      ["Misty", "Kanto", "85"],
      ["Brock", "Kanto", "80"],
      ["May", "Hoenn", "70"],
    ["Dawn", "Sinnoh", "68"],
    ["Iris", "Unova", "80"],
    ["Cilan", "Unova", "82"],
    ["Serena", "Calos", "66"],
    ["Kiawe", "Alola", "74"],
    ["Goh", "Kanto", "65"]



  ]
  with open("treinadores.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(treinadores_iniciais)

criar_arquivo_treinadores()


def ler_treinadores():
  treinadores = []
  with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
      treinadores.append(linha)
  return treinadores


def menu():
  treinadores = ler_treinadores()

  while True:
    print("\n===== TREINADORES POKÉMON =====")
    print("1 - Listar todos os treinadores")
    print("2 - Buscar treinador pelo nome")
    print("3 - Listar treinadores de uma região")
    print("4 - Mostrar treinador com maior nível")
    print("5 - Mostrar treinador com menor nível")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
      for t in treinadores:
        print(f"Nome: {t['nome']} | Região: {t['regiao']} | Nível: {t['nivel']}")


    elif opcao == "2":
      nome_busca = input("Digite o nome do treinador: ").lower()
      encontrou = False

      for t in treinadores:
        if t["nome"].lower() == nome_busca:
          print(
              f"Encontrado! Nome: {t['nome']} | Região: {t['regiao']} | Nível:"
              f" {t['nivel']}"
          )
          encontrou = True
          break

      if not encontrou:
        print("Treinador não encontrado.")

    elif opcao == "3":
      regiao_busca = input("Digite a região: ").lower()
      encontrou = False

      for t in treinadores:
        if t["regiao"].lower() == regiao_busca:
          print(f"- {t['nome']} (Nível: {t['nivel']})")
          encontrou = True

      if not encontrou:
        print("Nenhum treinador encontrado nessa região.")

    elif opcao == "4":
      maior = treinadores[0]
      for t in treinadores:
        if int(t["nivel"]) > int(maior["nivel"]):
          maior = t
      print(f"Treinador com maior nível: {maior['nome']} (Nível {maior['nivel']})")


    elif opcao == "5":
      menor = treinadores[0]
      for t in treinadores:
        if int(t["nivel"]) < int(menor["nivel"]):
          menor = t
      print(f"Treinador com menor nível: {menor['nome']} (Nível {menor['nivel']})")


    elif opcao == "6":
      print("Programa encerrado.")
      break

    else:
      print("Opção inválida! Escolha um número de 1 a 6.")



menu()