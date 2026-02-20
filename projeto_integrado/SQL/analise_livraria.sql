-- Consulta listando todos os livros
SELECT id, titulo, preco, data_publicacao, autor_id, estoque
FROM livraria_livro;

-- Consulta filtrando livros com estoque menor que 9.
SELECT *
FROM livraria_livro
WHERE estoque < 9;

-- Consulta ordenando livros por preço.
SELECT *
FROM livraria_livro ll 
ORDER BY ll.preco;

-- Consulta contando livros por autor.
SELECT la.nome, COUNT(*) AS 'Total de livros por autor'
FROM livraria_livro ll 
JOIN livraria_autor la
	ON ll.autor_id = la.id
GROUP BY 1;

-- Consulta com JOIN entre Livro e Autor.
SELECT ll.*, la.*
FROM livraria_livro ll
JOIN livraria_autor la 
	ON LL.autor_id = la.id;

-- Consulta calculando média de preço.
SELECT AVG(ll.preco) AS media_preco
from livraria_livro ll;
