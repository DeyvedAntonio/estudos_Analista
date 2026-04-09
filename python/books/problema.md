# Exercício Prático — Sistema Web de Controle de Biblioteca

## 1) Problema

Uma pequena biblioteca quer sair do controle manual em papel e planilhas soltas para um **sistema web** onde funcionários possam cadastrar livros, registrar membros, controlar empréstimos e acompanhar devoluções.

O objetivo é permitir que a equipe acesse tudo pelo navegador, com segurança, organização e dados centralizados em banco de dados.

---

## 2) Objetivo do sistema

Desenvolver um sistema web com Django para:

- cadastrar livros
- cadastrar usuários da biblioteca
- registrar empréstimos e devoluções
- consultar o status dos livros
- controlar o histórico de movimentações

---

## 3) Requisitos funcionais

Os requisitos funcionais descrevem **o que o sistema deve fazer**.

### RF01 — Autenticação de usuários

O sistema deve permitir que funcionários façam **login** para acessar a área administrativa.

### RF02 — Cadastro de livros

O sistema deve permitir cadastrar livros com os seguintes dados:

- título
- autor
- categoria
- ISBN
- ano de publicação
- quantidade disponível

### RF03 — Listagem de livros

O sistema deve listar todos os livros cadastrados, com opção de visualizar detalhes.

### RF04 — Cadastro de membros

O sistema deve permitir cadastrar os membros da biblioteca com:

- nome
- e-mail
- telefone
- documento de identificação

### RF05 — Empréstimo de livros

O sistema deve permitir registrar o empréstimo de um livro para um membro, informando:

- livro
- membro
- data do empréstimo
- data prevista de devolução

### RF06 — Devolução de livros

O sistema deve permitir registrar a devolução de um livro emprestado.

### RF07 — Controle de disponibilidade

O sistema deve impedir o empréstimo de livros que estejam sem exemplares disponíveis.

### RF08 — Histórico de movimentações

O sistema deve exibir o histórico de empréstimos e devoluções.

### RF09 — Edição e exclusão

O sistema deve permitir editar e excluir registros de livros e membros.

---

## 4) Requisitos não funcionais

Os requisitos não funcionais descrevem **como o sistema deve funcionar**.

### RNF01 — Interface web

O sistema deve ser acessado via navegador.

### RNF02 — Segurança de acesso

Somente usuários autenticados devem acessar as funcionalidades internas.

### RNF03 — Persistência de dados

Os dados devem ser armazenados em banco de dados.

### RNF04 — Usabilidade

A interface deve ser simples, clara e fácil de usar por funcionários sem conhecimento técnico.

### RNF05 — Responsividade básica

As páginas devem ser visualizadas corretamente em computador e tablet.

### RNF06 — Manutenibilidade

O código deve ser organizado seguindo a estrutura padrão do Django.

### RNF07 — Escalabilidade inicial

O sistema deve permitir futuras melhorias, como relatórios e filtros de busca.

---

## 5) Histórias de usuário

As histórias de usuário ajudam a pensar no sistema do ponto de vista de quem vai usar.

### História 1 — Login do funcionário

**Como funcionário da biblioteca,**  
quero fazer login no sistema,  
**para acessar as funcionalidades protegidas.**

### História 2 — Cadastro de livro

**Como funcionário da biblioteca,**  
quero cadastrar livros no sistema,  
**para manter o acervo organizado e atualizado.**

### História 3 — Consulta de livros

**Como funcionário da biblioteca,**  
quero visualizar a lista de livros cadastrados,  
**para localizar rapidamente um título.**

### História 4 — Cadastro de membro

**Como funcionário da biblioteca,**  
quero cadastrar membros,  
**para registrar quem pode realizar empréstimos.**

### História 5 — Empréstimo de livro

**Como funcionário da biblioteca,**  
quero registrar empréstimos,  
**para controlar quais livros estão com cada membro.**

### História 6 — Devolução de livro

**Como funcionário da biblioteca,**  
quero registrar devoluções,  
**para liberar o livro para novos empréstimos.**

### História 7 — Bloqueio de empréstimo sem estoque

**Como funcionário da biblioteca,**  
quero que o sistema bloqueie empréstimos de livros indisponíveis,  
**para evitar inconsistências no controle do acervo.**

### História 8 — Histórico de operações

**Como funcionário da biblioteca,**  
quero consultar o histórico de empréstimos e devoluções,  
**para acompanhar o movimento dos livros.**

---

## 6) Desafios técnicos esperados no exercício

Esse exercício é bom porque te faz praticar conceitos que aparecem logo no curso e também evoluem depois:

- criação de projeto Django
- criação de apps
- models e banco de dados
- migrations
- admin do Django
- formulários
- views
- templates
- autenticação
- relacionamento entre tabelas

---

## 7) Sugestão de escopo mínimo para começar

Se quiser fazer em etapas, comece assim:

### Etapa 1

- criar projeto Django
- criar app principal
- configurar banco
- criar modelos de livro e membro

### Etapa 2

- criar cadastro e listagem de livros
- usar Django Admin para testar os dados

### Etapa 3

- criar empréstimos e devoluções
- bloquear livros sem estoque

### Etapa 4

- implementar login
- proteger as rotas

---

## 8) Critério de sucesso do exercício

O exercício estará bem resolvido se o sistema permitir:

- login de funcionário
- cadastro de livros e membros
- empréstimo e devolução de livros
- atualização automática da disponibilidade
- consulta do histórico
