alunos = []
disciplinas = []
professores = []
turmas = []
matriculas = []

def exibir_menu_principal():
    print("\nMenu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

def exibir_menu_operacoes():
    print("\nMenu de Operações:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")

def listar_alunos():
    print("\nAlunos cadastrados:")
    if alunos:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")
    else:
        print("Nenhum aluno cadastrado.")

def incluir_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    alunos.append({'nome': nome, 'matricula': matricula})
    print("Aluno cadastrado com sucesso!")

def listar_disciplinas():
    print("\nDisciplinas cadastradas:")
    if disciplinas:
        for disciplina in disciplinas:
            print(f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}")
    else:
        print("Nenhuma disciplina cadastrada.")

def incluir_disciplina():
    nome = input("Digite o nome da disciplina: ")
    codigo = input("Digite o código da disciplina: ")
    disciplinas.append({'nome': nome, 'codigo': codigo})
    print("Disciplina cadastrada com sucesso!")

def listar_professores():
    print("\nProfessores cadastrados:")
    if professores:
        for professor in professores:
            print(f"Nome: {professor['nome']}, ID: {professor['id']}")
    else:
        print("Nenhum professor cadastrado.")

def incluir_professor():
    nome = input("Digite o nome do professor: ")
    id_professor = input("Digite o ID do professor: ")
    professores.append({'nome': nome, 'id': id_professor})
    print("Professor cadastrado com sucesso!")

def listar_turmas():
    print("\nTurmas cadastradas:")
    if turmas:
        for turma in turmas:
            print(f"Código: {turma['codigo']}, Disciplina: {turma['disciplina']}, Professor: {turma['professor']}")
    else:
        print("Nenhuma turma cadastrada.")

def incluir_turma():
    codigo = input("Digite o código da turma: ")
    disciplina = input("Digite o nome da disciplina da turma: ")
    professor = input("Digite o nome do professor da turma: ")
    turmas.append({'codigo': codigo, 'disciplina': disciplina, 'professor': professor})
    print("Turma cadastrada com sucesso!")

def listar_matriculas():
    print("\nMatrículas realizadas:")
    if matriculas:
        for matricula in matriculas:
            print(f"Aluno: {matricula['aluno']}, Turma: {matricula['turma']}")
    else:
        print("Nenhuma matrícula realizada.")

def incluir_matricula():
    aluno = input("Digite o nome do aluno: ")
    turma = input("Digite o código da turma: ")
    matriculas.append({'aluno': aluno, 'turma': turma})
    print("Matrícula realizada com sucesso!")

def main():
    while True:
        exibir_menu_principal()
        opcao_principal = input("Selecione uma opção: ")

        if opcao_principal == '6':
            print("Saindo do sistema...")
            break

        if opcao_principal not in ['1', '2', '3', '4', '5']:
            print("Opção inválida. Por favor, selecione uma opção válida.")
            continue

        opcao_principal = int(opcao_principal)

        while True:
            exibir_menu_operacoes()
            operacao = input("Selecione uma operação: ")

            if operacao == '5':
                break

            if operacao not in ['1', '2', '3', '4']:
                print("Opção inválida. Por favor, selecione uma operação válida.")
                continue

            operacao = int(operacao)

            if opcao_principal == 1:  # Estudantes
                if operacao == 1:
                    incluir_aluno()
                elif operacao == 2:
                    listar_alunos()
            elif opcao_principal == 2:  # Disciplinas
                if operacao == 1:
                    incluir_disciplina()
                elif operacao == 2:
                    listar_disciplinas()
            elif opcao_principal == 3:  # Professores
                if operacao == 1:
                    incluir_professor()
                elif operacao == 2:
                    listar_professores()
            elif opcao_principal == 4:  # Turmas
                if operacao == 1:
                    incluir_turma()
                elif operacao == 2:
                    listar_turmas()
            elif opcao_principal == 5:  # Matrículas
                if operacao == 1:
                    incluir_matricula()
                elif operacao == 2:
                    listar_matriculas()

if __name__ == "__main__":
    main()