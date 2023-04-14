import operacoesBD

def login_usuario(email: str, senha: str):
    # Construir consulta no BD
    # Criar condição para procurar no BD o e-mail e bater a senha
    #Caso não encontre, retornar false
    return 

def cadastrar_usuario(nome_completo: str, email: str, senha: str):
    # Validar informações (exemplo: verificar se email é único)
    if email == operacoesBD.consulta_banco(email):
        # Cadastrar usuário no banco de dados (exemplo: salvar em arquivo, inserir no banco de dados, etc.)
        usuario = {
            'nome': nome_completo,
            'email': email,
            'senha': senha
        }
        operacoesBD.inclusao_banco(usuario)
        print("Usuário cadastrado com sucesso!")
    else:
        print("Este email já está em uso. Por favor, tente novamente.")
    return print("Usuário cadastrado com sucesso!")

