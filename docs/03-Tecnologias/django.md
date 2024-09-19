# API de Apresentação Django

A **API de Apresentação** para esta prova de conceito foi desenvolvida utilizando o framework **Django**, com o propósito de servir como um **CMS** para a geração de manifestos de imagens IIIF . A escolha do Django se deu por sua facilidade de implementação e pelas funcionalidades integradas que simplificam a criação de APIs, além de fornecer uma interface administrativa automática para controle de conteúdo e sistemas de autenticação e autorização, facilitando o gerenciamento do sistema.

## Visão Geral

A API de Apresentação se integra com o servidor de imagens **Cantaloupe** para fornecer os manifestos IIIF que descrevem e disponibilizam imagens e metadados dos objetos IIIF.

## Estrutura do Projeto

Dentro da pasta `django` temos a seguinte estrutura de arquivos:

- **app/**
  - **models.py**: Modelos de dados do Django.
  - **utils.py**: Funções úteis, incluindo a geração de manifestos.
  - **views.py**: Página do Mirador.
- **digital_collection/**
  - **settings.py**: Configurações de banco de dados, autenticação, etc.
  - **urls.py**: Endpoints do projeto.
- **requirements.txt**: Lista de dependências.
- **manage.py**: Script de gerenciamento do Django.

### Principais Componentes

- **Modelos (Models):** Definem as estruturas de dados para armazenar informações sobre as imagens, manifestos e metadados.
- **Views:** Interagem com os modelos para fornecer os dados para o usuário.
- **URLs:** Definem os endpoints da API e mapeiam as URLs para as views correspondentes.

## Principais Endpoints

Nesta implementação, a API de Apresentação Django possui três endpoints principais:

1. **`/`**:

   - **Descrição:** Interface integrada com o Mirador.
   - **Função:** Permite a visualização das imagens através dos manifestos gerados.

2. **`/manifest/<id>`**:

   - **Descrição:** Endpoint para acessar um manifesto específico.
   - **Função:** Retorna o manifesto IIIF correspondente ao `<id>` fornecido.

3. **`/admin`**:
   - **Descrição:** Interface administrativa do Django.
   - **Função:** Permite gerenciar os manifestos, imagens e estruturas associadas.

### Configuração do Ambiente de Desenvolvimento

1. Instalação das Dependências:

```bash
pip install -r requirements.txt
```

2. Configuração do Banco de Dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

3. Migrações do Banco de Dados:

```bash
python manage.py migrate
```

1. Criação de administrador:

```bash
python manage.py createsuperuser
```

1. Execução do servidor:

```bash
python manage.py runserver
```
