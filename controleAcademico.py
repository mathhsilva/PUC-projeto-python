# Matheus Cordeiro da Silva
# Análise e Desenvolvimento de Sistemas
import json

# Nomes dos arquivos JSON (Utilizado para salvar os arquivos e recuperar após a finalização do sistema.)
ALUNOS_FILE = 'alunos.json'
DISCIPLINAS_FILE = 'disciplinas.json'
PROFESSORES_FILE = 'professores.json'
TURMAS_FILE = 'turmas.json'
MATRICULAS_FILE = 'matriculas.json'

# Função para carregar dados de um arquivo JSON
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

# Carregar dados ao iniciar o sistema
alunos = carregar_dados(ALUNOS_FILE)
disciplinas = carregar_dados(DISCIPLINAS_FILE)
professores = carregar_dados(PROFESSORES_FILE)
turmas = carregar_dados(TURMAS_FILE)
matriculas = carregar_dados(MATRICULAS_FILE)

# Função para exibir o menu principal
def exibir_menu_principal():
    print("\nMenu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

# Função para exibir o menu de operações
def exibir_menu_operacoes():
    print("\nMenu de Operações:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar (EM DESENVOLVIMENTO!)")
    print("4. Excluir (EM DESENVOLVIMENTO!)")
    print("5. Voltar ao menu principal")

# Função para listar os alunos cadastrados
def listar_alunos():
    print("\nAlunos cadastrados:")
    if alunos:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")
    else:
        print("Nenhum aluno cadastrado.")

# Função para incluir um novo aluno
def incluir_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    alunos.append({'nome': nome, 'matricula': matricula})
    salvar_dados(ALUNOS_FILE, alunos)
    print("Aluno cadastrado com sucesso!")

# Função para listar as disciplinas cadastradas
def listar_disciplinas():
    print("\nDisciplinas cadastradas:")
    if disciplinas:
        for disciplina in disciplinas:
            print(f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}")
    else:
        print("Nenhuma disciplina cadastrada.")

# Função para incluir uma nova disciplina
def incluir_disciplina():
    nome = input("Digite o nome da disciplina: ")
    codigo = input("Digite o código da disciplina: ")
    disciplinas.append({'nome': nome, 'codigo': codigo})
    salvar_dados(DISCIPLINAS_FILE, disciplinas)
    print("Disciplina cadastrada com sucesso!")

# Função para listar os professores cadastrados
def listar_professores():
    print("\nProfessores cadastrados:")
    if professores:
        for professor in professores:
            print(f"Nome: {professor['nome']}, ID: {professor['id']}")
    else:
        print("Nenhum professor cadastrado.")

# Função para incluir um novo professor
def incluir_professor():
    nome = input("Digite o nome do professor: ")
    id_professor = input("Digite o ID do professor: ")
    professores.append({'nome': nome, 'id': id_professor})
    salvar_dados(PROFESSORES_FILE, professores)
    print("Professor cadastrado com sucesso!")

# Função para listar as turmas cadastradas
def listar_turmas():
    print("\nTurmas cadastradas:")
    if turmas:
        for turma in turmas:
            print(f"Código: {turma['codigo']}, Disciplina: {turma['disciplina']}, Professor: {turma['professor']}")
    else:
        print("Nenhuma turma cadastrada.")

# Função para incluir uma nova turma
def incluir_turma():
    codigo = input("Digite o código da turma: ")
    disciplina = input("Digite o nome da disciplina da turma: ")
    professor = input("Digite o nome do professor da turma: ")
    turmas.append({'codigo': codigo, 'disciplina': disciplina, 'professor': professor})
    salvar_dados(TURMAS_FILE, turmas)
    print("Turma cadastrada com sucesso!")

# Função para listar as matrículas realizadas
def listar_matriculas():
    print("\nMatrículas realizadas:")
    if matriculas:
        for matricula in matriculas:
            print(f"Aluno: {matricula['aluno']}, Turma: {matricula['turma']}")
    else:
        print("Nenhuma matrícula realizada.")

# Função para incluir uma nova matrícula
def incluir_matricula():
    aluno = input("Digite o nome do aluno: ")
    turma = input("Digite o código da turma: ")
    matriculas.append({'aluno': aluno, 'turma': turma})
    salvar_dados(MATRICULAS_FILE, matriculas)
    print("Matrícula realizada com sucesso!")

# Função principal que controla o fluxo do programa
def main():
    while True:
        # Exibe o menu principal e obtém a opção do usuário
        exibir_menu_principal()
        opcao_principal = input("Selecione uma opção: ")

        # Se a opção for '6', o sistema encerra
        if opcao_principal == '6':
            print("Saindo do sistema...")
            break

        # Verifica se a opção selecionada é válida
        if opcao_principal not in ['1', '2', '3', '4', '5']:
            print("Opção inválida. Por favor, selecione uma opção válida.")
            continue

        # Converte a opção principal para inteiro
        opcao_principal = int(opcao_principal)

        # Loop para operações dentro da categoria selecionada
        while True:
            # Exibe o menu de operações e obtém a operação do usuário
            exibir_menu_operacoes()
            operacao = input("Selecione uma operação: ")

            # Se a operação for '5', volta ao menu principal
            if operacao == '5':
                break

            # Verifica se a operação selecionada é válida
            if operacao not in ['1', '2', '3', '4']:
                print("Opção inválida. Por favor, selecione uma operação válida.")
                continue

            # Converte a operação para inteiro
            operacao = int(operacao)

            # Verifica a categoria selecionada e executa a operação correspondente
            if opcao_principal == 1:  # Estudantes
                if operacao == 1:
                    incluir_aluno()
                elif operacao == 2:
                    listar_alunos()
                elif operacao in [3, 4]:
                    print("EM DESENVOLVIMENTO!")
                    break
            elif opcao_principal == 2:  # Disciplinas
                if operacao == 1:
                    incluir_disciplina()
                elif operacao == 2:
                    listar_disciplinas()
                elif operacao in [3, 4]:
                    print("EM DESENVOLVIMENTO!")
                    break
            elif opcao_principal == 3:  # Professores
                if operacao == 1:
                    incluir_professor()
                elif operacao == 2:
                    listar_professores()
                elif operacao in [3, 4]:
                    print("EM DESENVOLVIMENTO!")
                    break
            elif opcao_principal == 4:  # Turmas
                if operacao == 1:
                    incluir_turma()
                elif operacao == 2:
                    listar_turmas()
                elif operacao in [3, 4]:
                    print("EM DESENVOLVIMENTO!")
                    break
            elif opcao_principal == 5:  # Matrículas
                if operacao == 1:
                    incluir_matricula()
                elif operacao == 2:
                    listar_matriculas()
                elif operacao in [3, 4]:
                    print("EM DESENVOLVIMENTO!")
                    break

# Executa a função principal quando o script é executado diretamente
if __name__ == "__main__":
    main()