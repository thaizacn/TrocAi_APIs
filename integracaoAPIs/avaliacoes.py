import integracaoBD

def avaliacao_plataforma(id_usuario: int, comentario: str, nota: int):
    integracaoBD.InclusaoBanco.adicionar_avalicao_plataforma(comentario, nota, id_usuario)
    return {"message": "Avaliação registrada com sucesso!"} 

def avaliacao_operacao(id_usuario: int, id_operacao: int, comentario: str, nota: int):
    integracaoBD.InclusaoBanco.adicionar_avalicao_operacao(comentario, nota, id_operacao, id_usuario)
    return {"message": "Avaliação registrada com sucesso!"} 
