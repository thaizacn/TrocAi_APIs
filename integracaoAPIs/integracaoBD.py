from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Usuarios, Itens, AvaliacoesPlataforma, Operacoes, Mensagens, AvaliacoesOperacao
from PIL import image

SQLALCHEMY_DATABASE_URL = "mysql://adm_trocai:123456@localhost:3306/trocai"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base.metadata.create_all(engine)

# criando sessão com o Banco de Dados
Session = sessionmaker(bind=engine)
session = Session()

def consulta_banco(any):
    pass


class InclusaoBanco():
    def __init__(self):
        pass
    
    @classmethod
    def adicionar_usuario(self, nome, email, senha, imagem=None):
        novo_usuario = Usuarios(nome=nome, email=email, senha=senha, imagem=imagem)
        session.add(novo_usuario)
        session.commit()
        
    @classmethod
    def adicionar_item(self, item, descricao, id_usuario, imagem):
        novo_item = Itens(item=item, descricao=descricao, id_usuario=id_usuario, imagem=imagem)
        session.add(novo_item)
        session.commit()
        
    @classmethod
    def adicionar_avalicao_plataforma(self, conteudo, nota, id_usuario):
        nova_avaliacao_plataforma = AvaliacoesPlataforma(conteudo=conteudo, nota=nota, id_usuario=id_usuario)
        session.add(nova_avaliacao_plataforma)
        session.commit()

    @classmethod
    def adicionar_operacao(self, id_item, id_item_2):
        nova_operacao = Operacoes(id_item=id_item, id_item_2=id_item_2)
        session.add(nova_operacao)
        session.commit()

    @classmethod
    def adicionar_mensagem(self, conteudo, id_remetente, id_destinatario):
        nova_mensagem = Mensagens(onteudo=conteudo, id_remetente=id_remetente, id_destinatario=id_destinatario)
        session.add(nova_mensagem)
        session.commit()
        
    @classmethod
    def adicionar_avalicao_operacao(self, comentario, nota, id_operacao, id_usuario):
        nova_avaliacao_operacao = AvaliacoesOperacao(comentario=comentario, nota=nota, id_operacao=id_operacao, id_usuario=id_usuario)
        session.add(nova_avaliacao_operacao)
        session.commit()
        


## teste de consulta (SELECT)

# resultados = session.query(Usuarios).all()

# for resultado in resultados:
#     print('ID:',resultado.id)
#     print('Nome: ',resultado.nome)
#     print('E-mail: ', resultado.email)
#     print('Senha: ', resultado.senha)
#     print('################')

##

InclusaoBanco.adicionar_usuario('Carlos', 'carlos@gmail.com', 'senhasenha')

