
def login_usuario(email: str, senha: str):
    # Construir consulta no BD
    # Criar condição para procurar no BD o e-mail e bater a senha
    #Caso não encontre, retornar false
    return 

def cadastrar_usuario(nome_completo: str, email: str, confirmacao_email: str, senha: str, confirmacao_senha: str):
    # Validar informações (exemplo: verificar se email é único)
    if verificar_email(email):
        # Cadastrar usuário no banco de dados (exemplo: salvar em arquivo, inserir no banco de dados, etc.)
        usuario = {
            'nome': nome_completo,
            'email': email,
            'senha': senha
        }
        inclusao_banco(usuario)
        print("Usuário cadastrado com sucesso!")
    else:
        print("Este email já está em uso. Por favor, tente novamente.")
    return print("Usuário cadastrado com sucesso!")


def verificar_email(email):
    # Lógica para verificar se o email é único no sistema CONSULTANDO O BD
    return True

# TO-DO lógica para adicionar no BD
def inclusao_banco(any):
    pass

def registrar_produto(item: str, descricao: str, data_entrada: str):
    inclusao_banco(item, descricao, data_entrada)
    return print("Produto incluído com sucesso!")
