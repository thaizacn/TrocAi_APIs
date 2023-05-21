from fastapi import UploadFile, APIRouter
from fastapi.responses import FileResponse
from services import produto_service

router = APIRouter()

@router.post("/registrar_produto")
def registro_produto(item: str, descricao: str, id_usuario: int, imagem: UploadFile = None):
    return produto_service.registrar_produto(item, descricao, id_usuario, imagem)

@router.get("/consultar_registro")
def consulta_registro(id_usuario: int):
    return produto_service.consulta_produto(id_usuario)

@router.get("/pesquisar_itens")
def pesquisa_itens(pesquisa: str):
    return produto_service.pesquisa_itens(pesquisa)

@router.get("/consultar_imagem")
def consulta_imagem(id_usuario: int, item_id: int):
    return FileResponse(produto_service.consulta_imagem(id_usuario, item_id))