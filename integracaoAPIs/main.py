from fastapi import FastAPI, HTTPException, status, UploadFile
from fastapi.responses import JSONResponse
import services

app = FastAPI()

@app.get("/login")
def login(email: str, senha: str):
    return services.login_usuario(email, senha)

@app.post("/cadastro")
def cadastro(nome_completo: str, nome_usuario: str, email: str, confirmacao_email: str, senha: str, confirmacao_senha: str):
    if email == confirmacao_email and senha == confirmacao_senha:
        #TO-DO nome de usuário único: voltará none
        return services.cadastrar_usuario(nome_completo, nome_usuario, email, senha)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email e senha não coincidem, favor revisar")

@app.post("/registro")
def registro_produto(item: str, descricao: str, id: int, imagem: UploadFile = None):
    return services.registrar_produto(item, descricao, id, imagem)

@app.post("/mensagem")
def mensagem(conteudo: str, id_remetente: int, id_destinatario: int):
    return services.mensagem(conteudo, id_remetente, id_destinatario)

@app.post("/avaliacao_plataforma")
def avaliacao_plataforma(conteudo: str, nota: int, id_usuario: int):
    return services.avaliacao_plataforma(conteudo, nota, id_usuario)

@app.post("/avaliacao_operacao")
def avaliacao_operacao(id_item: int, id_item_2: int, id_receptor: int):
    return services.avaliacao_operacao(id_item, id_item_2, id_receptor)

@app.get("/consulta_operacao")
def consulta_operacao(id_usuario: int):
    return JSONResponse(services.consulta_operacao(id_usuario))

@app.get("/consulta_feed")
def consulta_feed():
    return services.consulta_feed()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)