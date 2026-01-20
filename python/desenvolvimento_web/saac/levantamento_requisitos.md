# Levantamento de Requisitos

Sistema de Agendamento e Atendimento de Clientes - SAAC

## 1. Visão Geral do Projeto

O sistema tem como objetivo permitir o agendamento, gestão e execução de atendimentos de clientes, atendendo diferentes segmentos como salões de beleza, barbearias, escritórios, clínicas e serviços Home Care.

Nesta fase, o foco é preparar o ambiente de desenvolvimento Django que dará suporte a esse sistema, garantindo uma base técnica estável, reproduzível e organizada para evolução futura.

## 2. Stakeholders Principais

- Cliente Final
    Usuário que realiza agendamentos e acompanha seus atendimentos.

- Profissional / Prestador de Serviço
    Responsável por atender clientes, visualizar agenda e registrar atendimentos.

- Administrador do Sistema
    Responsável por configurar usuários, serviços, agendas e regras de acesso.

## 3. Escopo Funcional (Alto Nível)

Nesta etapa, os requisitos são descritos sem implementação, apenas como necessidade do sistema.

### 3.1 Parte Administrativa — Requisitos Funcionais

O sistema deverá permitir:

- Controle de acesso de usuários com diferentes perfis

- Cadastro e gerenciamento de clientes

- Identificação de clientes VIP, com regras específicas de visualização

- Cadastro de profissionais (prestadores de serviço)

- Cadastro de grupos de profissionais

- Cadastro de especialidades profissionais

- Cadastro de serviços e/ou produtos

- Definição de valores de serviços e produtos por vigência

- Gerenciamento de agendas e escalas por profissional ou grupo

- Criação de atendimentos com ou sem agendamento prévio

- Possibilidade de alteração de horários de agendamento

- Aceitação ou recusa de solicitações de agendamento

- Opção de agendamento via dispositivos móveis ou desktop

- Possibilidade futura de envio de notificações por WhatsApp ou e-mail

### 3.2 Parte Operacional — Requisitos Funcionais

O sistema deverá permitir ao profissional:

- Visualizar agenda por período selecionado

- Exibir lista de clientes agendados com informações essenciais

- Acessar a área do cliente a partir do agendamento

- Visualizar dados do atendimento vigente

- Criar, cancelar, liberar ou consultar formulários de atendimento

- Visualizar histórico de atendimentos do cliente por data e profissional

- Exibir formulário ativo de atendimento durante a execução do serviço

## 4. Requisitos Não Funcionais (iniciais)

O sistema deverá ser acessado via navegador web

A interface deverá ser responsiva (desktop e mobile)

O acesso aos dados deverá respeitar regras de permissão

O sistema deverá possuir arquitetura em camadas (interface, backend e banco)

O ambiente de desenvolvimento deverá ser reproduzível em qualquer máquina

## 5. Requisitos Técnicos — Semana 03 (Escopo Controlado)

⚠️ Importante: os requisitos abaixo não são do sistema final, mas da preparação do ambiente, conforme definido na Semana 03.

### 5.1 Ambiente de Desenvolvimento

O projeto deverá:

- Utilizar Python com ambiente virtual isolado

- Ter dependências instaladas exclusivamente dentro do ambiente virtual

- Utilizar Django como framework backend

- Permitir execução local sem conflitos de dependências

### 5.2 Estrutura Inicial Esperada

O ambiente deverá conter:

ambiente_django/
├── venv/
└── projeto_django/
    ├── manage.py
    └── projeto_django/

## 7. Observação Importante

Este levantamento não autoriza ainda:

- Criação de apps Django

- Criação de models

- Escrita de views ou templates

- Configuração de banco de dados

Essas etapas só devem ser iniciadas após a conclusão formal da Semana 03.
