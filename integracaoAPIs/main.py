from fastapi import FastAPI
import implement

app = FastAPI()

@app.get("/login")
def login(email: str, senha: str):
    return 

@app.post("/cadastro")
def cadastro(nome_completo: str, data_nascimento: str, email: str, confirmacao_email: str, senha: str, confirmacao_senha: str):
    if email == confirmacao_email & senha == confirmacao_email:
        implement.cadastrar_usuario(nome_completo, data_nascimento, email, senha)
        return
    else:
        print("Email e senha não coincidem, favor revisar")