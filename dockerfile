# Use a imagem oficial do Python baseada em Debian
FROM python:3.11-slim-buster

# Define a diretório de trabalho no Docker
WORKDIR /integracapAPIs

# Atualiza o sistema e instala o MySQL client
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Instala as dependências do projeto
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o Docker
COPY . /integracapAPIs

# Comando para iniciar a aplicação
CMD ["uvicorn", "integracaoAPIs.main:app", "--host", "0.0.0.0", "--port", "8500"]
