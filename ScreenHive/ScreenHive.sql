CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    data_cadastro DATE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE Conteudo (
    id_conteudo INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    ano_lancamento DATE,
    duracao INT, -- Duração em minutos
    classificacao_indicativa VARCHAR(10),
    sinopse TEXT
);

CREATE TABLE Genero (
    id_genero INT PRIMARY KEY,
    nome VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE ContGenero (
    id_conteudo INT NOT NULL,
    id_genero INT NOT NULL,
    PRIMARY KEY (id_conteudo, id_genero), -- Chave primária composta 
    FOREIGN KEY (id_conteudo) REFERENCES Conteudo(id_conteudo) ON DELETE CASCADE,
    FOREIGN KEY (id_genero) REFERENCES Genero(id_genero) ON DELETE CASCADE
);

CREATE TABLE Avaliacao (
    id_avaliacao INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_conteudo INT NOT NULL,
    nota INT CHECK (nota >= 0 AND nota <= 5), -- nota de 0 a 5
    comentario TEXT,
    data_avaliacao DATE,
    UNIQUE (id_usuario, id_conteudo), -- Um usuário só pode avaliar um conteúdo uma vez
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_conteudo) REFERENCES Conteudo(id_conteudo) ON DELETE CASCADE
);

CREATE TABLE ListaPessoal (
    id_lista INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nome_lista VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

CREATE TABLE ItemLista (
    id_lista INT NOT NULL,
    id_conteudo INT NOT NULL,
    PRIMARY KEY (id_lista, id_conteudo),
    FOREIGN KEY (id_lista) REFERENCES ListaPessoal(id_lista) ON DELETE CASCADE,
    FOREIGN KEY (id_conteudo) REFERENCES Conteudo(id_conteudo) ON DELETE CASCADE
);

CREATE TABLE HistVisualizacao (
    id_historico INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_conteudo INT NOT NULL,
    concluido BOOLEAN DEFAULT FALSE,
    data_ultima_visualizacao DATE,
    UNIQUE (id_usuario, id_conteudo), -- Cada conteúdo aparece apenas uma vez no histórico de um usuário
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_conteudo) REFERENCES Conteudo(id_conteudo) ON DELETE CASCADE
);

CREATE TABLE Visualizacao (
    id_visualizacao INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_conteudo INT NOT NULL,
    minutos_assistidos INT NOT NULL,
    data_visualizacao DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_conteudo) REFERENCES Conteudo(id_conteudo) ON DELETE CASCADE
);

CREATE TABLE Recomendacao (
    id_recomendacao INT PRIMARY KEY,
    id_usuario_recomenda INT NOT NULL, -- Quem recomenda
    id_usuario_recebe INT NOT NULL,    -- Quem recebe
    id_conteudo INT NOT NULL,
    mensagem TEXT,
    data_recomendacao DATE,
    FOREIGN KEY (id_usuario_recomenda) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_usuario_recebe) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_conteudo) REFERENCES Conteudo(id_conteudo) ON DELETE CASCADE
);

CREATE TABLE Seguidores (
    id_seguidor INT NOT NULL, -- O usuário que segue
    id_seguido INT NOT NULL,  -- O usuário que está sendo seguido
    PRIMARY KEY (id_seguidor, id_seguido),
    FOREIGN KEY (id_seguidor) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_seguido) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- INSERCAO DE DADOS
-- Tabela Usuario
INSERT INTO Usuario (id_usuario, nome, data_nascimento, email, data_cadastro, senha) VALUES
(1, 'Ana Souza', '1990-05-10', 'ana@email.com', '2024-01-01', 'senha123'),
(2, 'Carlos Lima', '1985-11-25', 'carlos@email.com', '2024-01-02', 'senha123'),
(3, 'Mariana Dias', '1993-07-15', 'mariana@email.com', '2024-01-03', 'senha123'),
(4, 'Pedro Silva', '2000-04-20', 'pedro@email.com', '2024-01-04', 'senha123'),
(5, 'Joana Prado', '1988-09-30', 'joana@email.com', '2024-01-05', 'senha123'),
(6, 'Lucas Pereira', '1995-02-14', 'lucas@email.com', '2024-01-06', 'senha123'),
(7, 'Fernanda Alves', '1992-03-11', 'fernanda@email.com', '2024-01-07', 'senha123'),
(8, 'Ricardo Moura', '1987-06-08', 'ricardo@email.com', '2024-01-08', 'senha123'),
(9, 'Paula Castro', '1998-12-19', 'paula@email.com', '2024-01-09', 'senha123'),
(10, 'Gabriel Monteiro', '1991-08-03', 'gabriel@email.com', '2024-01-10', 'senha123');

-- Tabela Conteudo
INSERT INTO Conteudo (id_conteudo, titulo, tipo, ano_lancamento, duracao, classificacao_indicativa, sinopse) VALUES
(1, 'Sentimental Value', 'Filme', '2025-05-01', 120, '12', 'Drama entre pai e filha'),
(2, 'Flow', 'Filme', '2024-09-10', 90, 'L', 'A vida dos animais na floresta até que...'),
(3, 'WestWorld', 'Serie', '2016-01-15', 60, 'L', 'Avanços tecnológicos modernos.'),
(4, 'Anora', 'Filme', '2024-07-23', 120, '16', 'Humor na cidade grande.'),
(5, 'Odisseia', 'Filme', '2016-03-05', 180, '16', 'Civilizações antigas.'),
(6, 'Sex Education', 'Serie', '2019-11-11', 40, '12', 'Desafios no ensino médio.'),
(7, 'The Substance', 'Filme', '2024-10-31', 130, '18', 'Segredos em uma vila isolada.'),
(8, 'Masterchef', 'Serie', '2021-06-20', 25, 'L', 'Sabores da culinária brasileira.'),
(9, 'Dune', 'Filme', '2021-04-14', 130, '12', 'Batalhas no espaço.'),
(10, 'Procurando Nemo', 'Filme', '2003-12-01', 50, 'L', 'Oceano e suas criaturas.');

-- Tabela Genero
INSERT INTO Genero (id_genero, nome) VALUES
(1, 'Aventura'),
(2, 'Documentário'),
(3, 'Série'),
(4, 'Comédia'),
(5, 'Histórico'),
(6, 'Drama'),
(7, 'Mistério'),
(8, 'Culinária'),
(9, 'Ficção Científica'),
(10, 'Natureza');

-- Tabela ContGenero
INSERT INTO ContGenero (id_conteudo, id_genero) VALUES
(1, 6), (2, 1),
(2, 10), (3, 3),
(4, 4), (5, 1), 
(5, 5), (6, 3), 
(6, 6), (7, 7),
(8, 8), (9, 9),
(10, 2);

-- Tabela Avaliacao
INSERT INTO Avaliacao (id_avaliacao, id_usuario, id_conteudo, nota, comentario, data_avaliacao) VALUES
(1, 1, 1, 5, 'Muito bom!', '2025-06-01'),
(2, 2, 2, 4, 'Gostei bastante.', '2025-06-02'),
(3, 3, 3, 3, 'Regular.', '2025-06-03'),
(4, 4, 4, 2, 'Não curti.', '2025-06-04'),
(5, 5, 5, 4, 'Informativo.', '2025-06-05'),
(6, 6, 6, 5, 'Muito bom.', '2025-06-06'),
(7, 7, 7, 3, 'Ok.', '2025-06-07'),
(8, 8, 8, 5, 'Delicioso.', '2025-06-08'),
(9, 9, 9, 4, 'Empolgante.', '2025-06-09'),
(10, 10, 10, 5, 'Amei.', '2025-06-10');

-- Tabela ListaPessoal
INSERT INTO ListaPessoal (id_lista, id_usuario, nome_lista) VALUES
(1, 1, 'Favoritos'),
(2, 2, 'Assistir depois'),
(3, 3, 'Top 10'),
(4, 4, 'Meus filmes'),
(5, 5, 'Documentários'),
(6, 6, 'Dramas'),
(7, 7, 'Séries favoritas'),
(8, 8, 'Culinária'),
(9, 9, 'Natureza'),
(10, 10, 'Recomendados');

-- Tabela ItemLista
INSERT INTO ItemLista (id_lista, id_conteudo) VALUES
(1, 1), (1, 2),
(2, 3), (2, 4),
(3, 5), (4, 6), 
(4, 7), (5, 8),
(6, 9), (6, 10);

-- Tabela HistVisualizacao
INSERT INTO HistVisualizacao (id_historico, id_usuario, id_conteudo, concluido, data_ultima_visualizacao) VALUES
(1, 1, 1, TRUE, '2025-06-01'),
(2, 2, 2, TRUE, '2025-06-02'),
(3, 3, 3, FALSE, '2025-06-03'),
(4, 4, 4, TRUE, '2025-06-04'),
(5, 5, 5, TRUE, '2025-06-05'),
(6, 6, 6, FALSE, '2025-06-06'),
(7, 7, 7, TRUE, '2025-06-07'),
(8, 8, 8, FALSE, '2025-06-08'),
(9, 9, 9, TRUE, '2025-06-09'),
(10, 10, 10, FALSE, '2025-06-10');

-- Tabela Visualizacao
INSERT INTO Visualizacao (id_visualizacao, id_usuario, id_conteudo, minutos_assistidos, data_visualizacao) VALUES
(1, 1, 1, 120, '2025-06-01'),
(2, 2, 2, 45, '2025-06-02'),
(3, 3, 3, 15, '2025-06-03'),
(4, 4, 4, 90, '2025-06-04'),
(5, 5, 5, 60, '2025-06-05'),
(6, 6, 6, 40, '2025-06-06'),
(7, 7, 7, 110, '2025-06-07'),
(8, 8, 8, 25, '2025-06-08'),
(9, 9, 9, 130, '2025-06-09'),
(10, 10, 10, 50, '2025-06-10');

-- Tabela Recomendacao
INSERT INTO Recomendacao (id_recomendacao, id_usuario_recomenda, id_usuario_recebe, id_conteudo, mensagem, data_recomendacao) VALUES
(1, 1, 2, 1, 'Você vai curtir esse filme!', '2025-06-01'),
(2, 2, 3, 2, 'Muito bom, recomendo!', '2025-06-02'),
(3, 3, 4, 3, 'Esse é o seu estilo.', '2025-06-03'),
(4, 4, 5, 4, 'Assiste esse hoje!', '2025-06-04'),
(5, 5, 6, 5, 'Filme emocionante.', '2025-06-05'),
(6, 6, 7, 6, 'Tem tudo a ver com você.', '2025-06-06'),
(7, 7, 8, 7, 'Recomendo fortemente.', '2025-06-07'),
(8, 8, 9, 8, 'Vale a pena ver.', '2025-06-08'),
(9, 9, 10, 9, 'Você vai gostar.', '2025-06-09'),
(10, 10, 1, 10, 'Esse aqui é top!', '2025-06-10');

-- Tabela Seguidores
INSERT INTO Seguidores (id_seguidor, id_seguido) VALUES
(1, 2), (1, 3),
(2, 3), (2, 4),
(3, 1), (3, 5),
(4, 2), (5, 6),
(6, 1), (7, 2);

-- VISOES CRIADAS
CREATE OR REPLACE VIEW vw_resumo_atividade_usuario AS
SELECT u.id_usuario, u.nome, u.email, u.data_cadastro,
    (SELECT COUNT(*) FROM Avaliacao WHERE id_usuario = u.id_usuario) AS total_avaliacoes_feitas,
    (SELECT COUNT(*) FROM HistVisualizacao WHERE id_usuario = u.id_usuario AND concluido = TRUE) AS total_conteudos_concluidos,
    (SELECT COUNT(*) FROM Recomendacao WHERE id_usuario_recomenda = u.id_usuario) AS total_recomendacoes_enviadas,
    (SELECT COUNT(*) FROM ListaPessoal WHERE id_usuario = u.id_usuario) AS total_listas_criadas
FROM Usuario u ORDER BY u.id_usuario;

CREATE OR REPLACE VIEW vw_media_avaliacoes_conteudo AS
SELECT c.id_conteudo, c.titulo, c.tipo, c.ano_lancamento, COUNT(a.id_avaliacao) AS total_avaliacoes, ROUND(AVG(a.nota), 2) AS media_nota FROM Conteudo c
LEFT JOIN Avaliacao a ON c.id_conteudo = a.id_conteudo
GROUP BY c.id_conteudo, c.titulo, c.tipo, c.ano_lancamento
ORDER BY media_nota DESC, total_avaliacoes DESC;

-- USUARIOS CRIADOS
CREATE USER admin_app WITH PASSWORD 'senha123';
GRANT ALL PRIVILEGES ON DATABASE "ScreenHive" TO admin_app;

CREATE USER reader_user WITH PASSWORD 'senha123';
GRANT CONNECT ON DATABASE "ScreenHive" TO reader_app;
GRANT USAGE ON SCHEMA public TO reader_app;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader_app;
