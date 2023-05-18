from models import Usuarios
from fastapi import HTTPException, status
from fastapi import UploadFile
import shutil
import os
import integracaoBD 


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
        return {"message": "Usuário cadastrado com sucesso!", "id_usuario": {id}}
    
# REALIZA CONSULTA DE USUÁRIO
def consulta_usuario(email: str, senha: str):
    return integracaoBD.ConsultaBanco.consultar_dados_login(email, senha)

# REGISTRA AVALIAÇÃO SOBRE A PLATAFORMA
def avaliacao_plataforma(id_usuario: int, comentario: str, nota: int):
    integracaoBD.InclusaoBanco.adicionar_avalicao_plataforma(comentario, nota, id_usuario)
    return {"message": "Avaliação registrada com sucesso!"} 

# REGISTRA AVALIAÇÃO SOBRE A OPERAÇÃO
def avaliacao_operacao(id_usuario: int, id_operacao: int, comentario: str, nota: int):
    integracaoBD.InclusaoBanco.adicionar_avalicao_operacao(comentario, nota, id_operacao, id_usuario)
    return {"message": "Avaliação registrada com sucesso!"} 

# CONSULTA ID OPERAÇÃO
def consulta_operacao(id_usuario: int):
    return integracaoBD.ConsultaBanco.exibir_operacoes_realizadas(id_usuario)
    

# REGISTRA UM PRODUTO
def registrar_produto(item: str, descricao: str, id_usuario: int, imagem: UploadFile):
    if imagem is not None:
        # Salvar a imagem em um diretório específico
        pasta_destino = "img"
        nome_arquivo = imagem.filename
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
        caminho_arquivo = caminho_arquivo.replace("\\", "/")

    with open(caminho_arquivo, "wb") as arquivo_salvo:
            shutil.copyfileobj(imagem.file, arquivo_salvo)

    id_item = integracaoBD.InclusaoBanco.adicionar_item(item, descricao, id_usuario, caminho_arquivo)
    return {"message": "Item incluso com sucesso!", "id_item": {id_item}}

# ADICIONA MENSAGEM
def mensagens():
    integracaoBD.InclusaoBanco.adicionar_mensagem()
    return {"message": "Mensagem adicionada com sucesso!"} 