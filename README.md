# Prova de Conceito usando IIIF

Esse projeto é uma prova de conceito, com o objetivo de riar um sistema de imagens IIIF, utilizando o Cantaloupe como servidor de imagens, um banco de dados MySQL para armazenar os metadados das imagens e uma aplicação web Django para API de apresentação.

## Modelagem de dados

Precisamos de um banco de dados para armazenar os metadados das imagens para gerar os manifesto, para isso estou usando um banco de dados MySQL e o ORM do Django.

A modelagem conceitual foi feita usando o brModelo e exportada como xml. O arquivo xml está na pasta `docs`. A implementação usando o Django está declarada no arquivo `models.py`.

## Cantaloupe

Antes de servir a API de apresentação precisamos de um servidor de imagens IIIF, para isso estou usando o Cantaloupe, mais especificamente a imagem docker `edirom/cantaloupe` e suas configurações estão na pasta `cantaloupe`.

## API de apresentação

A API de apresentação é feita em Django, com o objetivo de servir os manifestos das imagens. A implementação está na pasta `django`.

### Configurações

Antes de rodar a API de apresentação **é necessário verificar as configurações de banco de dados** no arquivo `django/digital_collection/settings.py`. Por padrão o Django irá tentar se conectar com um banco de dados chamado `iiif_collection` com usuário `django_user` e senha `123456789`.

### Como rodar a API de apresentação

Para **rodar a API de apresentação sem o Docker** devemos:

1. Instalar o Python 3.8 (é necessário essa versão do Python para não ter problemas com o `prezi3_iiif`)
2. Navegar até a pasta `django` usando o comando `cd django`, se estiver na raiz do projeto.
3. Instalar as dependências do projeto usando o comando `pip install -r requirements.txt`. _Caso não funcione, tente `python -m pip install -r requirements.txt`_
4. Rode as migrações do banco de dados usando o comando `python manage.py migrate`.
5. Por fim, rode o servidor usando o comando `python manage.py runserver`.

## Rodando o projeto usando Docker

Para rodar o projeto usando o Docker, é necessário ter o **Docker e o Docker Compose instalados**.

1. Navegue até a raiz do projeto.
2. Rode o comando `docker-compose up --build`.
3. Acesse a API de apresentação em `http://localhost:8000/admin`.
4. Acesse o Cantaloupe em `http://localhost:8182/`.
