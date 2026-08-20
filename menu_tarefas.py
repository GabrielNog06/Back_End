tarefa = []

while True:
    print("Menu de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefa.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        print("Lista de Tarefas:")
        for i, t in enumerate(tarefa, start=1):
            print(f"{i}. {t}")
    elif opcao == "3":
        print("Atualizar Tarefa:")
        for i, t in enumerate(tarefa, start=1):
            print(f"{i}. {t}")
        indice = int(input("Digite o número da tarefa a ser atualizada: ")) - 1
        if 0 <= indice < len(tarefa):
            nova_tarefa = input("Digite a nova tarefa: ")
            tarefa[indice] = nova_tarefa
            print("Tarefa atualizada com sucesso!")
        else:
            print("Índice inválido.")
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")   