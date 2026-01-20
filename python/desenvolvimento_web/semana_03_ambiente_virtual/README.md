# Semana 03 — Ambientação e Instalação do Django com Poetry

# Projeto: SAAC (Sistema de Agendamento e Atendimento de Clientes)

## Objetivo da Semana

Preparar um ambiente de desenvolvimento Django estável, isolado e reproduzível, utilizando o Poetry como ferramenta de gerenciamento de dependências e ambientes virtuais.

Ao final desta semana, ser capaz de criar e executar o projeto SAAC do zero, compreendendo exatamente o papel de cada ferramenta e comando utilizado.

### Estrutura do Projeto

Estrutura esperada ao final da semana:

ambiente_django/
├── pyproject.toml
├── poetry.lock
└── saac/
    ├── manage.py
    └── saac/


O ambiente virtual é gerenciado automaticamente pelo Poetry.

## 1. Instalação do Poetry

Caso o Poetry ainda não esteja instalado no sistema:

`pip install poetry`


Verifique a instalação:

`poetry --version`

## 2. Criação do Ambiente do Projeto

Crie o diretório do projeto e acesse-o:

`mkdir ambiente_django
cd ambiente_django`


Inicialize o Poetry:

`poetry init`


Durante a inicialização:

- Aceite os valores padrão

- Não adicione dependências manualmente neste momento

Esse processo criará o arquivo pyproject.toml.

## 3. Instalação do Django com Poetry

Adicione o Django como dependência do projeto:

`poetry add django`


O Poetry irá:

- Criar automaticamente um ambiente virtual isolado

- Registrar o Django no pyproject.toml

- Gerar o arquivo poetry.lock, garantindo reprodutibilidade

## 4. Ativação do Ambiente Virtual

Ative o ambiente virtual gerenciado pelo Poetry:

´poetry shell´


A partir deste ponto, todos os comandos Python e Django estarão associados ao ambiente do projeto SAAC.

## 5. Criação do Projeto Django (SAAC)

Com o ambiente ativo, crie o projeto Django:

`poetry run django-admin startproject saac`


Esse comando cria:

- O arquivo manage.py

- O diretório principal de configurações do projeto SAAC

## 6. Execução do Servidor de Desenvolvimento

Acesse o diretório do projeto:

`cd saac`


Execute o servidor de desenvolvimento:

`poetry run python manage.py runserver`


Se não houver erros, o servidor estará disponível em:

http://127.0.0.1:8000/

A página padrão do Django deverá ser exibida no navegador.

## 7. Entendimento dos Componentes Utilizados

### Poetry

Responsável por:

- Gerenciar dependências

- Criar e controlar ambientes virtuais

- Garantir reprodutibilidade através do poetry.lock

### Django

Framework web utilizado como backend do sistema SAAC.

### django-admin

Ferramenta de linha de comando utilizada para criar e administrar projetos Django.

### manage.py

Script que executa comandos administrativos dentro do contexto do projeto Django.

### Servidor de Desenvolvimento

Servidor local fornecido pelo Django para testes durante o desenvolvimento.
Não deve ser utilizado em ambiente de produção.
