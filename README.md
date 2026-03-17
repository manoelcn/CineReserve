# 🎬 CineReserve

API REST para reserva de assentos em sessões de cinema, desenvolvida com Django e Django REST Framework.

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias](#-tecnologias)
- [Arquitetura](#-arquitetura)
- [Modelo de Dados](#-modelo-de-dados)
- [Endpoints da API](#-endpoints-da-api)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [Como Executar](#-como-executar)

---

## 💡 Sobre o Projeto

O **CineReserve** é uma aplicação backend que gerencia o fluxo completo de reserva de ingressos de cinema: desde a listagem de filmes e sessões disponíveis, passando pela reserva de assentos, até o checkout e a geração de tickets com código único.

---

## 🛠️ Tecnologias

| Tecnologia | Descrição |
|---|---|
| Python | Linguagem principal |
| Django | Framework web |
| Django REST Framework | Construção da API REST |
| PostgreSQL | Banco de dados relacional |
| psycopg2-binary | Driver PostgreSQL para Python |
| SimpleJWT | Autenticação via JWT |
| drf-spectacular | Geração automática de documentação |
| python-decouple | Gerenciamento de variáveis de ambiente |
| Poetry | Gerenciamento de dependências |
| Docker / Docker Compose | Containerização |

---

## 🏗️ Arquitetura

O projeto é dividido em três apps Django, cada um com responsabilidade bem definida:

```
CineReserve/
├── app/                  # Configurações do projeto (settings, urls, wsgi)
├── authentication/       # Cadastro e autenticação de usuários (JWT)
├── movies/               # Catálogo de filmes e sessões
├── reservations/         # Assentos, reservas, checkout e tickets
├── manage.py
├── pyproject.toml
└── docker-compose.yml
```

---

## 🔌 Endpoints da API

A documentação interativa completa está disponível em `/api/docs/` (Swagger UI) após subir a aplicação.

> ✅ Requer header `Authorization: Bearer <access_token>`

> ❌ Não Requer header `Authorization: Bearer <access_token>`

### 🔐 Autenticação — `/api/v1/authentication/`

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| `POST` | `/register/` | Cadastro de novo usuário | ❌ |
| `POST` | `/token/` | Login — obtém par de tokens JWT | ❌ |
| `POST` | `/token/refresh/` | Renova o access token | ❌ |
| `POST` | `/token/verify/` | Verifica validade de um token | ❌ |

### 📽️ Filmes — `/api/v1/`

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| `GET` | `/movies/` | Lista todos os filmes | ❌ |
| `GET` | `/movies/{movie_id}/sessions/` | Lista sessões de um filme | ❌ |

### 🎟️ Reservas — `/api/v1/`

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| `GET` | `/sessions/{session_id}/seats/` | Lista assentos de uma sessão | ❌ |
| `POST` | `/reservations/` | Cria uma reserva de assento | ✅ |
| `POST` | `/reservations/{reservation_id}/checkout/` | Confirma a reserva e gera o ticket | ✅ |
| `GET` | `/tickets/` | Lista tickets do usuário autenticado | ✅ |

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True

# PostgreSQL
DB_NAME=cinereserve
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db        # Use "db" com Docker, "localhost" sem Docker
DB_PORT=5432
```

Para gerar uma `SECRET_KEY` segura:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/manoelcn/CineReserve.git
cd CineReserve
```

**2. Configure as variáveis de ambiente**

```bash
cp .env.example .env
# Edite o .env com suas configurações
```

**3. Suba os containers**

```bash
docker compose up --build
```

> O Docker Compose irá subir dois serviços:
> - **`db`** — PostgreSQL 15, com healthcheck automático
> - **`web`** — Aplicação Django, aguarda o banco estar pronto e executa as migrations automaticamente antes de iniciar o servidor

**4. (Opcional) Crie um superusuário**

```bash
docker compose exec web python manage.py createsuperuser
```

**5. Acesse a aplicação**

| Serviço | URL |
|---|---|
| API | http://localhost:8000/api/v1/ |
| Swagger UI | http://localhost:8000/api/docs/ |
| Django Admin | http://localhost:8000/admin/ |

**Para encerrar os containers:**

```bash
docker compose down
```

**Para encerrar e remover os dados do banco:**

```bash
docker compose down -v
```

---

## 👤 Autor

Feito por **Manoel Cândido** — [GitHub](https://github.com/manoelcn)
