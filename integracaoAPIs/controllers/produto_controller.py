from fastapi import UploadFile, APIRouter, File, Form
from fastapi.responses import FileResponse
from services import produto_service
from fastapi.staticfiles import StaticFiles

router = APIRouter()

# Montar o diretório /img usando o StaticFiles
router.mount("/img", StaticFiles(directory="img"), name="img")

@router.post("/registrar_produto")
def registro_produto(item: str = Form(...), descricao: str = Form(...), id_usuario: int = Form(...), imagem: UploadFile = File(...)):
    return produto_service.registrar_produto(item, descricao, id_usuario, imagem)

@router.get("/consultar_registro")
def consulta_registro(id_usuario: int):
    return produto_service.consulta_produto(id_usuario)

@router.get("/pesquisar_itens")
def pesquisa_itens(pesquisa: str):
    return produto_service.pesquisa_itens(pesquisa)

@router.get("/img/{image_path}")
def get_imagem(image_path: str):
    return FileResponse(f"img/{image_path}")
