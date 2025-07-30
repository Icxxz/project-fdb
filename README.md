## Projeto de Fundamentos de banco de dados, ScreenHive, 2025.1
Professor: Francisco Victor da Silva Pinheiro \
Desenvolvido por Cícero Rodrigues da Silva Neto e Jeferson Mateus Lopes Alves. 

Plataforma de Streaming de Filmes: Ambiente digital onde usuários assistem filmes e séries, criam listas, avaliam e recebem recomendações personalizadas.
O projeto implementa uma plataforma de streaming inovadora que vai além do catálogo tradicional, oferecendo uma experiência personalizada para os usuários assistirem filmes e séries, criarem listas temáticas, avaliarem conteúdos, focando também na interação entre a comunidade, o que capacita aos usuários recomendarem entre si seus títulos prediletos ou seguirem uns aos outros.

O projeto foi construído utilizando as seguintes tecnologias:
  - Backend: Python 3.9+
  - Framework API: FastAPI
  - Banco de Dados: PostgreSQL
  - Driver de Conexão: Psycopg2
  - Servidor de Desenvolvimento: Uvicorn

Funcionalidades
  - Gerenciamento de Usuários: CRUD completo para usuários.
  - Catálogo de Conteúdo: Adição e consulta de filmes e séries.
  - Sistema de Avaliação: Usuários podem avaliar conteúdos com notas e comentários.
  - Listas Pessoais: Criação de listas personalizadas (ex: "Favoritos", "Assistir Mais Tarde").
  - Interação Social: Funcionalidades para seguir outros usuários e recomendar conteúdos.
  - Visões Complexas: Geração de relatórios diretamente do banco de dados, como ranking de conteúdos e resumo de atividade dos usuários.
  - Controle de Acesso: Níveis de permissão distintos para diferentes tipos de usuários.

Como funciona: \
  Tendo Python e o Postgres na sua maquina, clone o repositorio
  ```
  git clone https://github.com/Icxxz/project-fdb
  cd project-fdb
  ```
  Instale também as dependencias:
  `pip install fastapi uvicorn psycopg2-binary`\
  Configure o banco de dados, criando e povoando pelo arquivo ScreenHive.sql [Contribution guidelines for this project](ScreenHive/ScreenHive.sql) \
  Por fim, na pasta dos codigos, rode a main:
  `python -m uvicorn main:app --reload`

Após iniciar a aplicação, a documentação interativa da API, gerada automaticamente pelo Swagger UI, estará disponível em:\
http://127.0.0.1:8000/docs \
Através dessa interface, é possível testar todos os endpoints da API de forma visual e intuitiva.
