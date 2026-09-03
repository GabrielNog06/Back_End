# Lista de chamados
chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Computador não liga",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "hardware"
    },
    {
        "id": 4,
        "titulo": "Erro no sistema de e-mail",
        "prioridade": "baixa",
        "situacao": "fechado",
        "categoria": "software"
    },
    {
        "id": 5,
        "titulo": "Usuário sem acesso à rede",
        "prioridade": "média",
        "situacao": "aberto",
        "categoria": "acesso"
    }
]


# 1 - Listagem de todos os chamados
print("LISTA DE TODOS OS CHAMADOS")
print("------------------------------")

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("------------------------------")


# 2 - Filtro por situação existente
situacao_desejada = "aberto"
encontrou_chamado = False

print(f"\nCHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print("------------------------------")

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Categoria: {chamado['categoria']}")
        print("------------------------------")

        encontrou_chamado = True


if not encontrou_chamado:
    print("Nenhum chamado encontrado com essa situação.")


# 3 - Teste de filtro com situação inexistente
situacao_desejada = "cancelado"
encontrou_chamado = False

print(f"\nCHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print("------------------------------")

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print("------------------------------")

        encontrou_chamado = True


if not encontrou_chamado:
    print("Nenhum chamado encontrado com essa situação.")


# 4 - Atualização da situação por ID
id_procurado = 2
nova_situacao = "fechado"

encontrou_id = False

print(f"\nATUALIZANDO CHAMADO DE ID: {id_procurado}")

for chamado in chamados:
    if chamado["id"] == id_procurado:
        chamado["situacao"] = nova_situacao
        encontrou_id = True

        print("Situação atualizada com sucesso!")
        print(f"Nova situação: {chamado['situacao']}")

        break


if not encontrou_id:
    print("Chamado não encontrado.")


# 5 - Teste com ID inexistente
id_procurado = 10
nova_situacao = "aberto"

encontrou_id = False

print(f"\nATUALIZANDO CHAMADO DE ID: {id_procurado}")

for chamado in chamados:
    if chamado["id"] == id_procurado:
        chamado["situacao"] = nova_situacao
        encontrou_id = True

        print("Situação atualizada com sucesso!")

        break


if not encontrou_id:
    print("Chamado não encontrado.")


# 6 - Categorias sem repetição
categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])


print("\nCATEGORIAS SEM REPETIÇÃO")
print("------------------------------")

for categoria in categorias:
    print(categoria)