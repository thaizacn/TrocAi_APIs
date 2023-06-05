from repository import integracaoBD 

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