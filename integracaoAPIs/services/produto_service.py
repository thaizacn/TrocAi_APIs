from fastapi import UploadFile
import shutil
import os
from repository import integracaoBD 

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

# CONSULTA UM PRODUTO
def consulta_produto(id_usuario: int):
    return integracaoBD.ConsultaBanco.exibir_itens_usuario(id_usuario)

# PESQUISA POR PRODUTOS
def pesquisa_itens(pesquisa: str):
    return integracaoBD.ConsultaBanco.pesquisar_itens(pesquisa)

# CONSULTA IMAGEM DO PRODUTO
def consulta_imagem(id_usuario: int, item_id: int):
    imagem = integracaoBD.ConsultaBanco.exibir_imagem(id_usuario, item_id)
    # Retorna a imagem como resposta
    return imagem[0]