from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Usuarios

SQLALCHEMY_DATABASE_URL = "mysql://adm_trocai:123456@localhost:3306/trocai"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base.metadata.create_all(engine)

# criando sessão com o Banco de Dados
Session = sessionmaker(bind=engine)
session = Session()

# SELECT
resultados = session.query(Usuarios).all()

for resultado in resultados:
    print('ID:',resultado.id)
    print('Nome: ',resultado.nome)
    print('E-mail: ', resultado.email)
    print('Senha: ', resultado.senha)
    print('################')

# Base = declarative_base()