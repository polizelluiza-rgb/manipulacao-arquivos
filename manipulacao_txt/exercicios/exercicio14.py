def gerenciar_tarefas():
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            try:
                with open("tarefas.txt", "r", encoding="utf-8") as f:
                    print(f.read())
            except FileNotFoundError:
                print("O arquivo ainda não existe.")
        elif escolha == "2":
            texto = input("Digite o texto para adicionar: ")
            with open("tarefas.txt", "a", encoding="utf-8") as f:
                f.write(texto + "\n")
        elif escolha == "3":
            texto = input("Digite o texto para sobrescrever: ")
            with open("tarefas.txt", "w", encoding="utf-8") as f:
                f.write(texto + "\n")
        elif escolha == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")


gerenciar_tarefas()