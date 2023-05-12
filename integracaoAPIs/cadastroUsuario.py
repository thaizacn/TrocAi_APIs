from integracaoBD import session, ConsultaBanco, InclusaoBanco
from models import Usuarios
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException, status

def login_usuario(email: str, senha: str):
    if ConsultaBanco.consultar_dados_login(email, senha) == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário não consta na base, por favor, cadastre-se!")
    else:
        return {"message": "Usuário logado com sucesso!"}

def cadastrar_usuario(nome_completo: str, nome_usuario: str, email: str, senha: str):
    if session.query(Usuarios).filter(Usuarios.email == email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este email já está em uso. Por favor, tente novamente.")
    else:
        id = InclusaoBanco.adicionar_usuario(nome_completo, nome_usuario, email, senha)
        return {"message": "Usuário cadastrado com sucesso!", "id_usuario": {id}}

