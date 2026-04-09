# Modelagem do Banco de Dados — Sistema de Biblioteca

## 1) Entidades principais

A partir do exercício da biblioteca, as principais tabelas são:

- **Categoria**
- **Livro**
- **Membro**
- **Empréstimo**
- **Usuário do sistema** *(padrão do Django para autenticação)*

---

## 2) Tabela `Categoria`

### Objetivo

Organizar os livros em grupos.

### Campos

- `id` — chave primária
- `nome` — texto único
- `descricao` — texto opcional

### Relacionamento

- Uma categoria pode ter vários livros
- Um livro pertence a uma categoria

---

## 3) Tabela `Livro`

### Objetivo

Guardar os dados do acervo da biblioteca.

### Campos

- `id` — chave primária
- `titulo` — texto
- `autor` — texto
- `isbn` — texto único
- `ano_publicacao` — inteiro
- `quantidade_total` — inteiro
- `quantidade_disponivel` — inteiro
- `categoria_id` — chave estrangeira para `Categoria`

### Observação
O campo `quantidade_disponivel` ajuda a controlar empréstimos sem complicar a lógica.

---

## 4) Tabela `Membro`

### Objetivo
Armazenar os dados de quem pode pegar livros emprestados.

### Campos
- `id` — chave primária
- `nome` — texto
- `email` — texto único
- `telefone` — texto
- `documento` — texto único

---

## 5) Tabela `Emprestimo`

### Objetivo
Registrar os empréstimos e devoluções.

### Campos

- `id` — chave primária
- `livro_id` — chave estrangeira para `Livro`
- `membro_id` — chave estrangeira para `Membro`
- `data_emprestimo` — data
- `data_prevista_devolucao` — data
- `data_devolucao` — data opcional
- `status` — texto com valores como:
  - `emprestado`
  - `devolvido`
  - `atrasado`

### Observação

Essa tabela é o coração do sistema.  
Ela mostra quem pegou qual livro, quando pegou e se já devolveu.

---

## 6) Usuário do sistema

Para autenticação, o ideal é usar o **User padrão do Django**.

Assim, o funcionário faz login no sistema e acessa as funcionalidades protegidas.

---

## 7) Relacionamentos entre tabelas

### `Categoria` → `Livro`

- 1 categoria possui vários livros
- 1 livro pertence a 1 categoria

### `Livro` → `Emprestimo`

- 1 livro pode aparecer em vários empréstimos ao longo do tempo
- cada empréstimo pertence a 1 livro

### `Membro` → `Emprestimo`

- 1 membro pode ter vários empréstimos
- cada empréstimo pertence a 1 membro

---

## 8) Resumo em formato de tabela

### `Categoria`

| Campo | Tipo |
| ------ | ------ |
| id | int |
| nome | char |
| descricao | text |

### `Livro`

| Campo | Tipo |
| ------ | ------ |
| id | int |
| titulo | char |
| autor | char |
| isbn | char |
| ano_publicacao | int |
| quantidade_total | int |
| quantidade_disponivel | int |
| categoria_id | FK |

### `Membro`

| Campo | Tipo |
| ------ | ------ |
| id | int |
| nome | char |
| email | char |
| telefone | char |
| documento | char |

### `Emprestimo`

| Campo | Tipo |
| ------ | ------ |
| id | int |
| livro_id | FK |
| membro_id | FK |
| data_emprestimo | date |
| data_prevista_devolucao | date |
| data_devolucao | date null |
| status | char |

---

## 9) Regra de negócio importante

Antes de criar um empréstimo:

- verificar se `quantidade_disponivel > 0`

Ao devolver:

- preencher `data_devolucao`
- alterar o `status`
- aumentar a disponibilidade do livro

---

## 10) Conclusão

A modelagem do banco fica organizada com:

1. `Categoria`
2. `Livro`
3. `Membro`
4. `Emprestimo`

E a autenticação pode ser feita com o `User` padrão do Django.
