from fastapi import HTTPException, status, UploadFile, APIRouter
from services import usuario_service

router = APIRouter()

@router.post("/cadastrar_usuario")
def cadastro(nome_completo: str, nome_usuario: str, email: str, confirmacao_email: str, senha: str, confirmacao_senha: str):
    if email == confirmacao_email and senha == confirmacao_senha:
        #TO-DO nome de usuário único: voltará none
        return usuario_service.cadastrar_usuario(nome_completo, nome_usuario, email, senha)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email e senha não coincidem, favor revisar")
    
@router.get("/login")
def login(email: str, senha: str):
    return usuario_service.login_usuario(email, senha)

@router.post("/imagem_perfil")
def imagem_perfil(id_usuario: int, imagem: UploadFile = None):
    return usuario_service.imagem_perfil(id_usuario, imagem)

@router.get("/consultar_usuario")
def consulta_usuario(email: str):
    return usuario_service.consulta_usuario(email)