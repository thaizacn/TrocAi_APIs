from fastapi import FastAPI
from datetime import datetime
import implement

app = FastAPI()

@app.get("/login")
def login(email: str, senha: str):
    # atribuir variavel para devolver o return do metodo
    implement.login_usuario
    return 

@app.post("/cadastro")
def cadastro(nome_completo: str, email: str, confirmacao_email: str, senha: str, confirmacao_senha: str):
    if email == confirmacao_email & senha == confirmacao_email:
        # atribuir variavel para devolver o return do metodo
        implement.cadastrar_usuario(nome_completo, email, senha)
        return
    else:
        print("Email e senha não coincidem, favor revisar")

@app.post("/registro")
def registro_produto(item: str, descricao: str, data_entrada: str):
    #TO-DO amadurecer lógica para imagem
    data_formatada = datetime.strptime(data_entrada, "%d/%m/%Y")
    # atribuir variavel para devolver o return do metodo
    implement.registrar_produto(item, descricao, data_entrada)
    return 