import operacoesBD

def registrar_produto(item: str, descricao: str, data_entrada: str):
    operacoesBD.inclusao_banco(item, descricao, data_entrada)
    return print("Produto incluso com sucesso!")