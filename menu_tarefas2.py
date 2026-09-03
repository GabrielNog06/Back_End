tarefas = []

while True:
    print("\n--- MENU DE TAREFAS ---")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação de uma tarefa")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1 - CADASTRAR TAREFA
    if opcao == "1":
        titulo = input("Digite o título da tarefa: ").strip()
        prioridade = input(
            "Digite a prioridade (baixa, média ou alta): "
        ).lower()

        # Validar título
        if titulo == "":
            print("O título não pode estar vazio.")

        # Validar prioridade
        elif prioridade not in ["baixa", "média", "alta"]:
            print("Prioridade inválida. Escolha baixa, média ou alta.")

        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)

            print("Tarefa cadastrada com sucesso!")

    # OPÇÃO 2 - LISTAR TAREFAS
    elif opcao == "2":

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")

        else:
            print("\n--- LISTA DE TAREFAS ---")

            for i, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{i} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    # OPÇÃO 3 - ATUALIZAR SITUAÇÃO
    elif opcao == "3":
        numero = input(
            "Digite o número da tarefa que deseja concluir: "
        )

        # Verificar se foi digitado um número
        if numero.isdigit():

            # Converter para índice da lista
            indice = int(numero) - 1

            # Verificar se a tarefa existe
            if indice >= 0 and indice < len(tarefas):

                tarefas[indice]["situacao"] = "concluída"

                print("Tarefa marcada como concluída!")

            else:
                print("Tarefa inexistente.")

        else:
            print("Digite um número válido.")

    # OPÇÃO 4 - ENCERRAR
    elif opcao == "4":
        print("Sistema encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Escolha um número de 1 a 4.")