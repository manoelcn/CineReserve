# Usa uma imagem oficial do Python 3.12
FROM python:3.12-slim

# Define variáveis de ambiente para evitar arquivos .pyc e buffer de log
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema necessárias para o psycopg2 e Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copia os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock* /app/

# Configura o Poetry para não criar um ambiente virtual dentro do container
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia o restante do código da aplicação
COPY . /app/

# Expõe a porta que o Django usará
EXPOSE 8000

# Comando para rodar as migrações e iniciar o servidor (ajuste conforme necessário)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]