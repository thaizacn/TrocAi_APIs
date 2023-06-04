from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker, joinedload, aliased
from models.models import Base, Usuarios, Itens, AvaliacoesPlataforma, Operacoes, Mensagens, AvaliacoesOperacao

SQLALCHEMY_DATABASE_URL = "mysql://trocai_adm:Senha.123@localhost:3306/trocai"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base.metadata.create_all(engine)

# criando sessão com o Banco de Dados
Session = sessionmaker(bind=engine)
session = Session()

class ConsultaBanco():
    def __init__(cls):
        pass
    
    @classmethod
    def exibir_itens_feed(cls):
        feed = session.query(Itens).order_by(Itens.id.desc()).all()
        return feed

    @classmethod
    def pesquisar_itens(cls, pesquisa):
        itens_pesquisa = session.query(Itens).filter(or_(Itens.item.contains(pesquisa), Itens.descricao.contains(pesquisa))).all()
        return itens_pesquisa

    @classmethod
    def exibir_itens_usuario(cls, id_usuario):
        itens = session.query(Itens).\
            filter(Itens.id_usuario == id_usuario).\
            order_by(Itens.id.desc()).all()
        return itens

    @classmethod
    def exibir_mensagens(cls, id_remetente, id_destinatario):
        mensagens = session.query(Mensagens).\
            filter(or_(
                    and_(Mensagens.id_remetente == id_remetente, Mensagens.id_destinatario == id_destinatario),
                    and_(Mensagens.id_remetente == id_destinatario, Mensagens.id_destinatario == id_remetente))).\
            order_by(Mensagens.id.desc()).all()
        return mensagens

    @classmethod
    def exibir_operacoes_realizadas(cls, id_usuario):
        doacoes = session.query(Operacoes, Itens).\
            join(Usuarios, Usuarios.id == Operacoes.id_receptor).\
            join(Itens, Itens.id == Operacoes.id_item).\
            options(joinedload(Operacoes.usuarios)).\
            filter(Usuarios.id == id_usuario).all()

        itens1 = aliased(Itens)
        itens2 = aliased(Itens)
        trocas = session.query(Operacoes, itens1, itens2).\
            join(itens1, itens1.id == Operacoes.id_item).\
            join(itens2, itens2.id == Operacoes.id_item_2).\
            options(joinedload(Operacoes.usuarios)).\
            filter(or_(itens1.id_usuario == id_usuario, itens2.id_usuario == id_usuario)).all()

        return trocas, doacoes

    @classmethod
    def consultar_dados_login(cls, email, senha):
        usuario = session.query(Usuarios).filter(Usuarios.email == email, Usuarios.senha == senha).first()
        return usuario
    
    @classmethod
    def consultar_usuario(cls, email):
        usuario = session.query(Usuarios).filter(Usuarios.email == email).first()
        return usuario

    @classmethod
    def exibir_imagem(cls, id_usuario, item_id):
        imagem = session.query(Itens.imagem).filter(Itens.id_usuario == id_usuario, Itens.id == item_id).first()
        return imagem


class InclusaoBanco():
    def __init__(cls):
        pass

    @classmethod
    def adicionar_usuario(cls, nome, nome_usuario, email, senha, imagem=None):
        novo_usuario = Usuarios(nome_completo=nome, nome_de_usuario=nome_usuario, email=email, senha=senha, imagem=imagem)
        session.add(novo_usuario)
        session.commit()
        session.flush()
        session.refresh(novo_usuario)
        user_id = novo_usuario.id
        return user_id
    
    @classmethod
    def incluir_imagem(cls, id_usuario, imagem):
        usuario = session.query(Usuarios).filter(Usuarios.id == id_usuario).first()

        if usuario:
            # Atualiza o caminho da imagem
            usuario.imagem = imagem
            session.commit()
            session.refresh(usuario)
        
    @classmethod
    def adicionar_item(cls, item, descricao, id_usuario, imagem):
        novo_item = Itens(item=item, descricao=descricao, id_usuario=id_usuario, imagem=imagem)
        session.add(novo_item)
        session.commit()
        session.flush()
        session.refresh(novo_item)
        item_id = novo_item.id
        return item_id
        
    @classmethod
    def adicionar_avalicao_plataforma(cls, conteudo, nota, id_usuario):
        nova_avaliacao_plataforma = AvaliacoesPlataforma(conteudo=conteudo, nota=nota, id_usuario=id_usuario)
        session.add(nova_avaliacao_plataforma)
        session.commit()

    @classmethod
    def adicionar_operacao(cls, id_item, id_item_2, id_receptor):
        nova_operacao = Operacoes(id_item=id_item, id_item_2=id_item_2, id_receptor=id_receptor)
        session.add(nova_operacao)
        session.commit()

    @classmethod
    def adicionar_mensagem(cls, conteudo, id_remetente, id_destinatario):
        nova_mensagem = Mensagens(conteudo=conteudo, id_remetente=id_remetente, id_destinatario=id_destinatario)
        session.add(nova_mensagem)
        session.commit()
        
    @classmethod
    def adicionar_avalicao_operacao(cls, comentario, nota, id_operacao, id_usuario):
        nova_avaliacao_operacao = AvaliacoesOperacao(comentario=comentario, nota=nota, id_operacao=id_operacao, id_usuario=id_usuario)
        session.add(nova_avaliacao_operacao)
        session.commit()


'''

## teste de inserção:

# Para inserir uma imagem, devemos transformar em um arquivo binário:
# Levar em conta o tamanho da imagem a ser armazenada

with open('imagem.png', 'rb') as file:
    image_bytes = file.read()
InclusaoBanco.adicionar_item('kit de ferramenta', 'pra você desmotar o que quiser', 1, image_bytes)
InclusaoBanco.adicionar_avalicao_plataforma('Não curti :/', 2, 5)
InclusaoBanco.adicionar_operacao(7, None, 3)
InclusaoBanco.adicionar_avalicao_operacao('Não voltaria a trocar', 2, 3, 1)
InclusaoBanco.adicionar_usuario('Celso', 'celso@gmail.com', '12345678', image_bytes)
InclusaoBanco.adicionar_mensagem('Testando :)', 1, 4)

## teste de consulta (SELECT)

consulta_login = ConsultaBanco.consultar_dados_login('luiz@email.com', 'senha123')
if not consulta_login:
    print("Email ou senha não correspondem.")
else:
    print("Login realizado com sucesso!")

    
feed = ConsultaBanco.exibir_itens_feed()

for post in feed:
    print(post.id)
    print(post.item)
    print(post.descricao)

itens = ConsultaBanco.exibir_itens_usuario(4)

for item in itens:
    print(item.id)
    print(item.item)
    print(item.descricao)


mensagens = ConsultaBanco.exibir_mensagens(5,3)

for mensagem in mensagens:
    print(mensagem.id)
    print(mensagem.conteudo)
    print(mensagem.data_envio)



pesquisa_itens = ConsultaBanco.pesquisar_itens('Lápis')

for pesquisa in pesquisa_itens:
    print(pesquisa.item)
    print(pesquisa.descricao)

consulta_trocas, consulta_doacoes = ConsultaBanco.exibir_operacoes_realizadas(1)


for operacao, itens in consulta_doacoes:
    print(
        f"Operação ID: {operacao.id} | "
        f"Item doado: {itens.item} | "
        f"Receptor: {operacao.usuarios.nome_completo}" 
        )

for operacao, item1, item2 in consulta_trocas:
    print(
        f"Operação ID: {operacao.id} | "
        f"Item 1: {item1.item} | "
        f"Item 2: {item2.item} | "
        f"Dono do Item 1: {item1.usuarios.nome_completo} | "
        f"Dono do Item 2: {item2.usuarios.nome_completo}"
    )

'''