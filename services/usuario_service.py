from models.models import Usuarios
from fastapi import HTTPException, status
from fastapi import UploadFile
import shutil
import os
from repository import integracaoBD 

# REALIZA O LOGIN DO USUÁRIO
def login_usuario(email: str, senha: str):
    if integracaoBD.ConsultaBanco.consultar_dados_login(email, senha) == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário não consta na base, por favor, cadastre-se!")
    else:
        return {"message": "Usuário logado com sucesso!"}

# REALIZA O CADASTRO DO USUÁRIO
def cadastrar_usuario(nome_completo: str, nome_usuario: str, email: str, senha: str):
    if integracaoBD.session.query(Usuarios).filter(Usuarios.email == email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este email já está em uso. Por favor, tente novamente.")
    else:
        id = integracaoBD.InclusaoBanco.adicionar_usuario(nome_completo, nome_usuario, email, senha)
        return {"message": "Usuário cadastrado com sucesso!", "id_usuario": id}
    
# INCLUI UMA IMAGEM NO PERFIL DO USUÁRIO
def imagem_perfil(id_usuario: int, imagem: UploadFile = None):
    if imagem is not None:
        # Salvar a imagem em um diretório específico
        pasta_destino = "img/perfil"
        nome_arquivo = imagem.filename
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
        caminho_arquivo = caminho_arquivo.replace("\\", "/")

    with open(caminho_arquivo, "wb") as arquivo_salvo:
            shutil.copyfileobj(imagem.file, arquivo_salvo)

    integracaoBD.InclusaoBanco.incluir_imagem(id_usuario, caminho_arquivo)
    return {"message": "Imagem inclusa com sucesso!"}
    
# CONSULTA USUARIO
def consulta_usuario(email: str):
    return integracaoBD.ConsultaBanco.consultar_usuario(email)