-- Exercícios
-- Autor: Deyved Antonio

-- Banco de dados: sqlite3

-- Nível básico
-- Exercício 1: Retorne o nome e o tipo de todos os filmes que foram lançados em 2022.
SELECT title, type FROM netflix_title WHERE release_year = 2022;

-- Exercício 2: Retorne o nome e o país de origem de todas as séries que foram adicionadas à Netflix em 2023.
SELECT title, country FROM netflix_title WHERE type = 'TV Show' AND release_year = 2023;

-- Nível intermediário
-- Exercício 3: Retorne o filme com a maior duração.
SELECT title, MAX(duration_min_seasons) as duracao_maxima FROM netflix_title WHERE type = 'Movie';

-- Exercício 4: Retorne as séries com a classificação média mais alta.


-- Nível avançado
-- Exercício 5: Retorne os filmes que foram dirigidos por um diretor que também dirigiu um filme que ganhou um Oscar.

-- Exercício 6: Retorne as séries que são mais populares em um determinado país.
