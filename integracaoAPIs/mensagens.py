import integracaoBD

def mensagens():
    integracaoBD.InclusaoBanco.adicionar_mensagem()
    return {"message": "Mensagem adicionada com sucesso!"} 