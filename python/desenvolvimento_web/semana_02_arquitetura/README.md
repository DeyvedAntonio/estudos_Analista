# Semana 02 — Arquitetura de Sistema Web

## 1. Visão Geral do Sistema

Este documento descreve a arquitetura de um Sistema de Agendamento e Atendimento de Clientes, aplicável a diferentes contextos como salão de beleza, barbearia, escritórios, clínicas e atendimentos Home Care.

O objetivo desta etapa é compreender e explicar a separação entre interface, backend e banco de dados, bem como o fluxo correto das informações dentro de um sistema web.

## 2. Arquitetura do Sistema

O sistema é estruturado em três camadas principais, cada uma com responsabilidades bem definidas.

<img width="655" height="412" alt="image" src="https://github.com/user-attachments/assets/79658e58-e830-4109-aaab-04bfd787a13c" />

### 2.1 Interface (Frontend)

A interface é responsável pela interação direta com o usuário final, permitindo:

- Cadastro de clientes e profissionais

- Agendamento de atendimentos

- Visualização de agendas e históricos

A interface é acessada via navegador, tanto em dispositivos móveis quanto em computadores, e não possui acesso direto ao banco de dados.

### 2.2 Backend (Django)

O backend, desenvolvido com Django, atua como camada intermediária e central do sistema, sendo responsável por:

- Receber os dados enviados pela interface

- Validar regras de negócio (permissões, disponibilidade de agenda, perfis de acesso)

- Processar atendimentos e agendamentos

- Controlar o acesso aos dados

- Gerenciar a comunicação com o banco de dados

O Django garante que todas as operações ocorram de forma segura, organizada e padronizada.

### 2.3 Banco de Dados (SQL)

O banco de dados tem como função:

- Armazenar de forma estruturada os dados do sistema

- Manter histórico de atendimentos e agendamentos

- Garantir integridade e consistência das informações

- Permitir consultas futuras para relatórios e análises

O banco não interage diretamente com o usuário, sendo acessado exclusivamente pelo backend.

## 3. Fluxo de Dados do Sistema

O fluxo de funcionamento segue o padrão abaixo:

`Usuário
  ↓
Interface (HTML)
  ↓
View Django
  ↓
Model Django
  ↓
Banco de Dados (SQL)`


Quando necessário, os dados retornam pelo mesmo caminho até a interface para exibição ao usuário.

## 4. Justificativa da Arquitetura

- O banco de dados não se comunica diretamente com o usuário para evitar falhas de segurança e inconsistências.

- O Django atua como intermediário obrigatório para centralizar regras de negócio, validações e controle de acesso.

- Os dados ficam prontos para análise futura quando estão corretamente estruturados e armazenados no banco de dados, podendo ser consultados por SQL ou ferramentas analíticas.

## 5. Contexto Funcional do Sistema (Exemplo)

Como exemplo de aplicação dessa arquitetura, o sistema contempla funcionalidades administrativas e operacionais, como:

Parte Administrativa

- Controle de acesso de usuários

- Cadastro de clientes, profissionais e especialidades

- Gerenciamento de agendas e escalas

- Definição de valores por vigência

- Regras de visibilidade (ex.: cliente VIP)

Parte Operacional Profissional

- Visualização de agenda por data

- Atendimento de clientes agendados

- Histórico de atendimentos por cliente

- Registro e consulta de informações do atendimento

## 6. Conclusão

Esta arquitetura garante:

- Organização do sistema

- Facilidade de manutenção

- Segurança dos dados

- Base sólida para crescimento e análises futuras
