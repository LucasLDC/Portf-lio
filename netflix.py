# Dicionários para armazenar os dados de filmes e usuários
filmes = {
    "A Ilha": {
        "Ano": "2004",
        "Sinopse": "Um homem e uma mulher lutam para escapar de uma utopia futurista que esconde um segredo sombrio."
    },
    "Matrix": {
        "Ano": "1999",
        "Sinopse": "Um hacker descobre uma realidade alternativa e luta contra seres opressores em um mundo distópico."
    },
    "Planeta dos Macacos: O Reinado": {
        "Ano": "2024",
        "Sinopse": "Em um mundo dominado por macacos inteligentes, um grupo de humanos luta pela sobrevivência."
    }
}

usuarios = {
    "joao.silva@example.com": {
        "Nome": "João Silva",
        "Idade": "28",
        "Telefone": "(11) 99999-9999",
        "Senha": "senha123"
    },
    "maria.oliveira@example.com": {
        "Nome": "Maria Oliveira",
        "Idade": "35",
        "Telefone": "(21) 88888-8888",
        "Senha": "123senha"
    },
    "carlos.santos@example.com": {
        "Nome": "Carlos Santos",
        "Idade": "42",
        "Telefone": "(31) 77777-7777",
        "Senha": "carlos42"
    }
}

# Função para cadastrar filmes
def cadastrar_filmes():
    while True:
        titulo = input("Informe o título do filme: ")
        ano_lancamento = input("Informe o ano de lançamento: ")
        sinopse = input("Informe a sinopse do filme: ")
        filmes[titulo] = {'Ano': ano_lancamento, 'Sinopse': sinopse}
        print(f"Filme '{titulo}' cadastrado com sucesso!\n")
        if input("Deseja cadastrar outro filme? (s/n): ").lower() == 'n':
            break

# Função para remover filmes
def remover_filmes():
    titulo = input("Informe o título do filme a ser removido: ")
    if titulo in filmes:
        del filmes[titulo]
        print(f"Filme '{titulo}' removido com sucesso!\n")
    else:
        print("Filme não encontrado.\n")

# Função para cadastrar usuários
def cadastrar_usuarios():
    while True:
        email = input("Informe o E-Mail do usuário: ")
        if email in usuarios:
            print("E-mail já cadastrado.\n")
            continue
        nome = input("Informe o nome do usuário: ")
        idade = input("Informe a idade do usuário: ")
        telefone = input("Informe o telefone do usuário: ")
        senha = input("Informe a senha do usuário: ")
        usuarios[email] = {'Nome': nome, 'Idade': idade, 'Telefone': telefone, 'Senha': senha}
        print(f"Usuário '{nome}' cadastrado com sucesso!\n")
        if input("Deseja cadastrar outro usuário? (s/n): ").lower() == 'n':
            break

# Função para remover usuários
def remover_usuarios():
    email = input("Informe o E-Mail do usuário a ser removido: ")
    if email in usuarios:
        del usuarios[email]
        print("Usuário removido com sucesso!\n")
    else:
        print("Usuário não encontrado.\n")

# Função para login do usuário
def login_usuario():
    email = input("Informe o E-Mail: ")
    senha = input("Informe a senha: ")
    if email in usuarios and usuarios[email]['Senha'] == senha:
        print("Login bem-sucedido!\n")
        listar_filmes()
    else:
        print("E-Mail ou senha incorretos.\n")

# Função para listar filmes
def listar_filmes():
    filmes_ordenados = sorted(filmes.keys())
    while True:
        print("0 – Sair do sistema")
        for i, titulo in enumerate(filmes_ordenados, 1):
            print(f"{i} – {titulo} – {filmes[titulo]['Ano']}")
        escolha = input("\nEscolha um filme pelo número ou '0' para sair: ")
        if escolha == '0':
            break
        elif escolha.isdigit() and 0 < int(escolha) <= len(filmes_ordenados):
            titulo_escolhido = filmes_ordenados[int(escolha) - 1]
            print(f"\n{filmes[titulo_escolhido]['Sinopse']}\n")
            if input("Deseja assistir? (s/n): ").lower() == 's':
                print("Bom Filme!\n")
        else:
            print("Opção inválida.\n")

# Menu principal
def menu_principal():
    while True:
        print("Menu Inicial:")
        print("1. Cadastro de Filmes")
        print("2. Cadastro de Usuários")
        print("3. Login do Usuário")
        print("4. Saída")
        opcao = input("Escolha uma opção: ").lower()
        if opcao == '1':
            cadastrar_filmes()
        elif opcao == '2':
            cadastrar_usuarios()
        elif opcao == '3':
            login_usuario()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o programa
if __name__ == "__main__":
    menu_principal()
    