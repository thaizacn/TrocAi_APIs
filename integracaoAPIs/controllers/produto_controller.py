from fastapi import UploadFile, APIRouter
from fastapi.responses import FileResponse
from services import produto_service
from fastapi.staticfiles import StaticFiles
import glob 

router = APIRouter()

# Montar o diretório /img usando o StaticFiles
router.mount("/img", StaticFiles(directory="img"), name="img")

@router.post("/registrar_produto")
def registro_produto(item: str, descricao: str, id_usuario: int, imagem: UploadFile = None):
    return produto_service.registrar_produto(item, descricao, id_usuario, imagem)

@router.get("/consultar_registro")
def consulta_registro(id_usuario: int):
    return produto_service.consulta_produto(id_usuario)

@router.get("/pesquisar_itens")
def pesquisa_itens(pesquisa: str):
    return produto_service.pesquisa_itens(pesquisa)

@router.get("/img/{image_path}")
def get_imagem(image_path: str):
    return FileResponse(image_path)
