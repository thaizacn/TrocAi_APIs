from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services import plataforma_service

router = APIRouter()

@router.post("/publicar_mensagem")
def mensagem(conteudo: str, id_remetente: int, id_destinatario: int):
    return plataforma_service.mensagens(conteudo, id_remetente, id_destinatario)

@router.get("/consultar_mensagem")
def consulta_mensagem(id_remetente: int, id_destinatario: int):
    return plataforma_service.consulta_mensagem(id_remetente, id_destinatario)

@router.post("/avaliar_plataforma")
def avaliacao_plataforma(conteudo: str, nota: int, id_usuario: int):
    return plataforma_service.avaliacao_plataforma(conteudo, nota, id_usuario)

@router.post("/avaliar_operacao")
def avaliacao_operacao(id_item: int, id_item_2: int, id_receptor: int):
    return plataforma_service.avaliacao_operacao(id_item, id_item_2, id_receptor)

@router.get("/consultar_operacao")
def consulta_operacao(id_usuario: int):
    return JSONResponse(plataforma_service.consulta_operacao(id_usuario))

@router.get("/consultar_feed")
def consulta_feed():
    return plataforma_service.consulta_feed()