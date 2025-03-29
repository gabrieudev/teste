<h1 align="center" style="font-weight: bold;">Testes de nivelamento 🧩</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D" alt="Vue">
  <img src="https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=AEDDFF" alt="Vuetify">
  <img src="https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres">
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

<p align="center">
 <a href="#estrutura">Estrutura do projeto</a> • 
 <a href="#executar">Como executar</a> •
 <a href="#extras">Extras</a>
</p>

<p align="center">
  <b>Repositório para os testes de nivelamento técnico envolvendo web scraping, transformação de dados, banco de dados e API REST com interface Vue.js.</b>
</p>

<h2 id="estrutura">📂 Estrutura do projeto</h2>

```yaml
├── backend/                  # Código Python (servidor, scraping, ETL)
│   ├── src/
│   │   ├── scraping/         # Scripts de web scraping (Teste 1)
│   │   ├── data_processing/  # Transformação de dados (Teste 2)
│   │   ├── api/              # Servidor Flask (Teste 4)
│   │   └── database/         # Scripts SQL e operações com o banco (Teste 3)
│   ├── data/                 # Arquivos gerados/baixados após executar o projeto
│   │   ├── pdfs/             # Anexos I e II
│   │   ├── csv/              # CSV do Teste 2 e dados da ANS
│   │   └── zip/              # Arquivos compactados
│   └── Dockerfile            # Dockerfile para o backend
│
├── frontend/                 # Interface Vue.js (Teste 4)
│   ├── src/
│   │   ├── components/       # Componentes Vue
│   │   ├── types/            # Interface de operadora
│   │   ├── views/            # Página
│   │   ├── router/           # Rota
│   │   ├── assets/           # SCSS
│   │   ├── plugins/          # Vuetify
│   │   └── App.vue
│   └── Dockerfile            # Dockerfile para o frontend
│
├── docs/                     # Documentação
│   └── postman/              # Coleção Postman (Teste 4.3)
│
└── docker-compose.yml        # Containerização (scripts, servidor, banco de dados e interface)
```

<h2 id="executar">🚀 Primeiros Passos</h2>

<h3>Pré-requisitos</h3>

- [Git](https://git-scm.com/downloads)
- [Docker Compose](https://docs.docker.com/compose/install/)

<h3>Clonar projeto</h3>

```bash
git clone https://github.com/gabrieudev/teste.git
```

<h3>Executar</h3>

```bash
cd teste
docker compose up -d --build
```

> O container `preprocessing` leva em torno de 2 minutos para finalizar a execução de todos os scripts.

<h3>Resultado</h3>

Acesse a interface em [http://localhost:8080](http://localhost:8080).

<h2 id="extras">➕ Extras</h2>

Além dos testes demandados, o projeto cumpriu os seguintes requisitos extras:

1. **Containerização:** A aplicação está totalmente containerizada, incluindo Docker Compose com todos os serviços necessários.
2. **Paginação:** É possível pesquisar as operadoras de maneira paginada, melhorando a experiência do usuário na interface.
