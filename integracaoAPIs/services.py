from models import Usuarios
from fastapi import HTTPException, status
from fastapi import UploadFile
import shutil
import os
import integracaoBD 
import json


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
    
# CONSULTA USUARIO
def consulta_usuario(email: str):
    return integracaoBD.ConsultaBanco.consultar_usuario(email)

# REGISTRA AVALIAÇÃO SOBRE A PLATAFORMA
def avaliacao_plataforma(conteudo: str, nota: int, id_usuario: int):
    integracaoBD.InclusaoBanco.adicionar_avalicao_plataforma(conteudo, nota, id_usuario)
    return {"message": "Avaliação registrada com sucesso!"} 

# REGISTRA AVALIAÇÃO SOBRE A OPERAÇÃO
def avaliacao_operacao(id_item: int, id_item_2: int, id_receptor: int):
    integracaoBD.InclusaoBanco.adicionar_avalicao_operacao(id_item, id_item_2, id_receptor)
    return {"message": "Avaliação registrada com sucesso!"} 

# CONSULTA OPERAÇÃO
def consulta_operacao(id_usuario: int):
    consulta_trocas, consulta_doacoes = integracaoBD.ConsultaBanco.exibir_operacoes_realizadas(id_usuario)

    # Lista para armazenar as operações de doação
    doacoes = []
    for operacao, itens in consulta_doacoes:
        doacao = {
            'Operação ID': operacao.id,
            'Item doado': itens.item,
            'Receptor': operacao.usuarios.nome_completo
        }
        doacoes.append(doacao)

    # Lista para armazenar as operações de troca
    trocas = []
    for operacao, item1, item2 in consulta_trocas:
        troca = {
            'Operação ID': operacao.id,
            'Item 1': item1.item,
            'Item 2': item2.item,
            'Dono do Item 1': item1.usuarios.nome_completo,
            'Dono do Item 2': item2.usuarios.nome_completo
        }
        trocas.append(troca)

    # Criar um dicionário contendo as listas de doações e trocas
    resultado = {
        'doacoes': doacoes,
        'trocas': trocas
    }

    return resultado
    

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
def mensagens(conteudo: str, id_remetente: int, id_destinatario: int):
    integracaoBD.InclusaoBanco.adicionar_mensagem(conteudo, id_remetente, id_destinatario)
    return {"message": "Mensagem adicionada com sucesso!"} 

# VISUALIZA MENSAGEM
def consulta_mensagem(id_remetente: int, id_destinatario: int):
    return integracaoBD.ConsultaBanco.exibir_mensagens(id_remetente, id_destinatario)

# CONSULTA FEED
def consulta_feed():
    return integracaoBD.ConsultaBanco.exibir_itens_feed()
    