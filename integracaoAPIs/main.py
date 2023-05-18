from fastapi import FastAPI, HTTPException, status, UploadFile
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
    
@app.get("/consulta_usuario")
def consulta_usuario(email: str, senha: str):
    return services.consulta_usuario(email, senha)    

@app.post("/registro")
def registro_produto(item: str, descricao: str, id: int, imagem: UploadFile = None):
    return services.registrar_produto(item, descricao, id, imagem)

@app.post("/mensagem")
def mensagem(id: int, comentario: str, nota: int):
    return services.mensagem(id, comentario, nota)

@app.post("/avaliacao_plataforma")
def avaliacao_plataforma(id: int, comentario: str, nota: int):
    return services.avaliacao_plataforma(id, comentario, nota)

@app.post("/avaliacao_operacao")
def avaliacao_operacao(id: int, id_operacao: int, comentario: str, nota: int):
    return services.avaliacao_operacao(id, id_operacao, comentario, nota)

@app.get("/consulta_operacao")
def consulta_operacao(id_usuario: int):
    return services.consulta_operacao(id_usuario)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)