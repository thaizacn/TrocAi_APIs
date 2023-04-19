from sqlalchemy import Column, ForeignKey, Integer, String, Table, LargeBinary, Date, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha = Column(String(20), index=True, nullable=False)
    imagem = Column(LargeBinary)


class Itens(Base):
    __tablename__ = "itens"

    # tabelas:
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    item = Column(String(50), index=True, nullable=False)
    descricao = Column(String(255), nullable=False)
    data_entrada = Column(Date, nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    imagem = Column(LargeBinary, nullable=False)

    # relacionamentos:
    usuarios = relationship('Usuarios', foreign_keys=[id_usuario])
    

class AvaliacoesPlataforma(Base):
    __tablename__ = "avaliacoes_plataforma"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    conteudo = Column(String(255), nullable=False)
    nota = Column(String(255), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuarios = relationship('Usuarios', foreign_keys=[id_usuario])


class Operacoes(Base):
    __tablename__ = "operacoes"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_item = Column(Integer, ForeignKey('itens.id'), nullable=False)
    id_item_2 = Column(Integer, ForeignKey('itens.id'))
    data_e_hora = Column(DateTime, nullable=False)

    itens = relationship('Itens', foreign_keys=[id_item])
    itens_2 = relationship('Itens',foreign_keys=[id_item_2])


class Mensagens(Base):
    __tablename__ = "mensagens"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    conteudo = Column(String(1000), nullable=False)
    id_remetente = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_destinatario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    data_envio = Column(DateTime, nullable=False)

    usuarios = relationship('Usuarios', foreign_keys=[id_remetente])
    usuarios_2 = relationship('Usuarios',foreign_keys=[id_destinatario])


class AvaliacoesOperacao(Base):
    __tablename__ = "avaliacoes_operacao"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    comentario = Column(String(255))
    nota = Column(Integer, nullable=False)
    id_operacao = Column(Integer, ForeignKey('operacoes.id'), nullable=False)
    id_usuario = Column(DateTime, ForeignKey('usuarios.id'), nullable=False)

    operacoes = relationship('Operacoes', foreign_keys=[id_operacao])
    usuarios = relationship('Usuarios',foreign_keys=[id_usuario])
# ...mapeamento de outras tabelas...