# ==========================================
# CONTROLE INTERNO DE TAREFAS
# ==========================================


# ==========================================
# CLASSE TAREFA
# ==========================================

class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.situacao = "Pendente"

    def concluir(self):
        self.situacao = "Concluída"

    def exibir_resumo(self):
        return (
            f"Título: {self.titulo} | "
            f"Prioridade: {self.prioridade} | "
            f"Situação: {self.situacao}"
        )


# ==========================================
# FUNÇÃO PARA CADASTRAR TAREFAS
# ==========================================

def cadastrar_tarefa(tarefas, titulo, descricao, prioridade):
    nova_tarefa = Tarefa(titulo, descricao, prioridade)

    tarefas.append(nova_tarefa)

    return nova_tarefa


# ==========================================
# FUNÇÃO PARA LISTAR TAREFAS
# ==========================================

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa.exibir_resumo()}")


# ==========================================
# FUNÇÃO PARA FILTRAR POR SITUAÇÃO
# ==========================================

def filtrar_por_situacao(tarefas, situacao):
    tarefas_filtradas = []

    for tarefa in tarefas:
        if tarefa.situacao == situacao:
            tarefas_filtradas.append(tarefa)

    return tarefas_filtradas


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

# Lista onde as tarefas serão armazenadas
tarefas = []


# ==========================================
# CADASTRO DE 3 TAREFAS
# ==========================================

cadastrar_tarefa(
    tarefas,
    "Revisar chamados",
    "Verificar chamados pendentes da equipe",
    "Alta"
)

cadastrar_tarefa(
    tarefas,
    "Atualizar manual interno",
    "Ajustar instruções de atendimento",
    "Média"
)

cadastrar_tarefa(
    tarefas,
    "Planejar reunião",
    "Preparar pauta da reunião semanal",
    "Baixa"
)


# ==========================================
# CONCLUIR UMA TAREFA
# ==========================================

tarefas[0].concluir()


# ==========================================
# LISTAR TODAS AS TAREFAS
# ==========================================

print("TODAS AS TAREFAS")
print("------------------------------")

listar_tarefas(tarefas)


# ==========================================
# FILTRAR TAREFAS CONCLUÍDAS
# ==========================================

print("\nTAREFAS CONCLUÍDAS")
print("------------------------------")

tarefas_concluidas = filtrar_por_situacao(
    tarefas,
    "Concluída"
)

listar_tarefas(tarefas_concluidas)


# ==========================================
# FILTRAR TAREFAS PENDENTES
# ==========================================

print("\nTAREFAS PENDENTES")
print("------------------------------")

tarefas_pendentes = filtrar_por_situacao(
    tarefas,
    "Pendente"
)

listar_tarefas(tarefas_pendentes)