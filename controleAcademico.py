import json

# Nomes dos arquivos JSON
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

# Função para incluir um novo registro
def incluir_registro(arquivo, dados_novos):
    dados = carregar_dados(arquivo)
    dados.append(dados_novos)
    salvar_dados(arquivo, dados)
    print(f"Registro cadastrado com sucesso em {arquivo}!")

# Função para listar os registros de um arquivo
def listar_registros(arquivo, mensagem_vazia):
    dados = carregar_dados(arquivo)
    print(f"\n{mensagem_vazia}:")
    if dados:
        for item in dados:
            print(item)
    else:
        print("Nenhum registro encontrado.")

# Função para atualizar um registro (em desenvolvimento)
def atualizar_registro(arquivo):
    print("Função de atualização em desenvolvimento!")

# Função para excluir um registro (em desenvolvimento)
def excluir_registro(arquivo):
    print("Função de exclusão em desenvolvimento!")

# Função principal que controla o fluxo do programa
def main():
    while True:
        # Exibe o menu principal
        print("\nMenu Principal:")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")

        # Obtém a opção do usuário
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

        # Define os arquivos e mensagens de acordo com a opção selecionada
        if opcao_principal == 1:
            arquivo = ALUNOS_FILE
            mensagem_vazia = "Nenhum aluno cadastrado."
        elif opcao_principal == 2:
            arquivo = DISCIPLINAS_FILE
            mensagem_vazia = "Nenhuma disciplina cadastrada."
        elif opcao_principal == 3:
            arquivo = PROFESSORES_FILE
            mensagem_vazia = "Nenhum professor cadastrado."
        elif opcao_principal == 4:
            arquivo = TURMAS_FILE
            mensagem_vazia = "Nenhuma turma cadastrada."
        elif opcao_principal == 5:
            arquivo = MATRICULAS_FILE
            mensagem_vazia = "Nenhuma matrícula realizada."

        # Loop para operações dentro da categoria selecionada
        while True:
            # Exibe o menu de operações
            print("\nMenu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Atualizar (EM DESENVOLVIMENTO!)")
            print("4. Excluir (EM DESENVOLVIMENTO!)")
            print("5. Voltar ao menu principal")

            # Obtém a operação do usuário
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

            # Executa a operação selecionada
            if operacao == 1:
                # Incluir novo registro
                if opcao_principal == 1:  # Estudantes
                    nome = input("Digite o nome do aluno: ")
                    matricula = input("Digite a matrícula do aluno: ")
                    incluir_registro(arquivo, {'nome': nome, 'matricula': matricula})
                elif opcao_principal == 2:  # Disciplinas
                    nome = input("Digite o nome da disciplina: ")
                    codigo = input("Digite o código da disciplina: ")
                    incluir_registro(arquivo, {'nome': nome, 'codigo': codigo})
                elif opcao_principal == 3:  # Professores
                    nome = input("Digite o nome do professor: ")
                    id_professor = input("Digite o ID do professor: ")
                    incluir_registro(arquivo, {'nome': nome, 'id': id_professor})
                elif opcao_principal == 4:  # Turmas
                    codigo = input("Digite o código da turma: ")
                    disciplina = input("Digite o nome da disciplina da turma: ")
                    professor = input("Digite o nome do professor da turma: ")
                    incluir_registro(arquivo, {'codigo': codigo, 'disciplina': disciplina, 'professor': professor})
                elif opcao_principal == 5:  # Matrículas
                    aluno = input("Digite o nome do aluno: ")
                    turma = input("Digite o código da turma: ")
                    incluir_registro(arquivo, {'aluno': aluno, 'turma': turma})

            elif operacao == 2:
                # Listar registros
                listar_registros(arquivo, mensagem_vazia)

            elif operacao == 3:
                # Atualizar registro
                atualizar_registro(arquivo)

            elif operacao == 4:
                # Excluir registro
                excluir_registro(arquivo)

# Executa a função principal quando o script é executado diretamente
if __name__ == "__main__":
    main()