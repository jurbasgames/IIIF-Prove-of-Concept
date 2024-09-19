# Prova de Conceito IIIF

Este projeto é uma prova de conceito com o objetivo de **criar um sistema de imagens IIIF**, utilizando o **Cantaloupe** como servidor de imagens, um banco de dados **MySQL** para armazenar os metadados das imagens e uma aplicação web **Django** para a API de apresentação.

## Índice

- [Prova de Conceito IIIF](#prova-de-conceito-iiif)
  - [Índice](#índice)
  - [Visão Geral](#visão-geral)
  - [Pré-requisitos](#pré-requisitos)
  - [Modelagem de Dados](#modelagem-de-dados)
  - [Servidor de Imagens Cantaloupe](#servidor-de-imagens-cantaloupe)
    - [Configuração do Cantaloupe](#configuração-do-cantaloupe)
  - [API de Apresentação Django](#api-de-apresentação-django)
    - [Configurações](#configurações)
    - [Como Rodar a API de Apresentação](#como-rodar-a-api-de-apresentação)
      - [Rodando Sem Docker](#rodando-sem-docker)
    - [Rodando com Docker](#rodando-com-docker)
      - [Rodando o Projeto usando Docker](#rodando-o-projeto-usando-docker)
  - [Referências](#referências)

## Visão Geral

Este projeto demonstra a implementação de um sistema de imagens conforme os padrões do **IIIF** (International Image Interoperability Framework). Utilizamos o **Cantaloupe** para servir as imagens, **MySQL** para o armazenamento de metadados e **Django** para gerenciar a API de apresentação dos manifestos IIIF.

## Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas:

- **Docker** e **Docker Compose**
- **Python 3.8**
- **MySQL**
- **Git**

## Modelagem de Dados

Para o armazenamento dos metadados das imagens e geração dos manifestos, utilizamos o banco de dados **MySQL** junto com o **Django ORM**. A modelagem conceitual foi realizada utilizando o **BrModelo** e exportada como XML. O arquivo XML está na pasta `docs/02-IIIF`. A implementação dos modelos no Django está declarada no arquivo `django/models.py`.

## Servidor de Imagens Cantaloupe

O **Cantaloupe** é um servidor de imagens de código aberto que implementa a **API de Imagem do IIIF**. Ele é escolhido por sua capacidade de servir imagens em alta qualidade e escalabilidade, além de ser fácil de configurar e manter.

### Configuração do Cantaloupe

Na prova de conceito, utilizamos a imagem Docker `edirom/cantaloupe`, facilitando a configuração através do arquivo `cantaloupe.properties`, localizado na pasta `docs/03-Tecnologias/cantaloupe.md`.

## API de Apresentação Django

A **API de Apresentação** foi desenvolvida utilizando o framework **Django**, servindo como um CMS para a geração de manifestos IIIF. A escolha do Django se deu por sua facilidade de implementação, oferecendo uma interface administrativa automática, sistemas de autenticação e autorização, o que facilita o gerenciamento do conteúdo.

### Configurações

Antes de rodar a API de apresentação, **é necessário verificar as configurações do banco de dados** no arquivo `django/digital_collection/settings.py`. Por padrão, o Django tentará se conectar com um banco de dados chamado `iiif_collection` com usuário `django_user` e senha `123456789`. As configurações podem ser ajustadas conforme necessário para o seu ambiente.

### Como Rodar a API de Apresentação

#### Rodando Sem Docker

1. **Instalar o Python 3.8:**

   - Certifique-se de ter o Python 3.8 instalado. Essa versão é necessária para evitar problemas com a dependência `prezi3_iiif`.

2. **Navegar até a Pasta `django`:**

   ```bash
   cd django
   ```

3. **Instalar as Dependências do Projeto:**

   ```bash
   pip install -r requirements.txt
   ```

   Caso o comando acima não funcione, tente:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Rodar as Migrações do Banco de Dados:**

   ```bash
   python manage.py migrate
   ```

5. **Executar o Servidor de Desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

### Rodando com Docker

#### Rodando o Projeto usando Docker

1. **Rodar o Docker Compose:**

   ```bash
   docker-compose up --build
   ```

2. **Acessar as Interfaces:**
   - API de Apresentação Django: [http://localhost:8000/admin](http://localhost:8000/admin)
   - Servidor de Imagens Cantaloupe: [http://localhost:8182/](http://localhost:8182/)

## Referências

- [Documentação Oficial do IIIF](https://iiif.io/)
- [Documentação do Cantaloupe](https://cantaloupe-project.github.io/)
- [Documentação do Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
