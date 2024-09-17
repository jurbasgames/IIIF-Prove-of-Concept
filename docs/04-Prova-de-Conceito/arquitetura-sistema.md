# Arquitetura do Sistema

## Visão Geral

A arquitetura deste sistema de imagens foi projetada para oferecer uma solução escalável e eficiente para a gestão e visualização de imagens digitais, utilizando os padrões do IIIF (International Image Interoperability Framework). O sistema integra duas APIs principais do IIIF: a **API de Imagem** e a **API de Apresentação**, garantindo alta qualidade na entrega de imagens e facilitando a interoperabilidade e a integração com diversos visualizadores.

## Diagrama de Arquitetura

![Diagrama](./arquitetura-diagrama.png)

_Figura 1: Diagrama de arquitetura do sistema de imagens IIIF_

## Componentes Principais

### 1. Frontend (Django + Mirador)

**Descrição:**
O frontend é responsável pela exibição das imagens e interação. Utiliza um visualizador compatível com IIIF, Mirador permitindo super zoom, camparação lado a lado etc.

**Tecnologias Utilizadas:**

- **Mirador:** Ferramenta de visualização que consome a nossa API de apresentação e imagem para exibir as imagens e metadados.

**Funcionalidades:**

- Carregamento dinâmico de imagens via IIIF API de Imagem.
- Exibição de metadados e imagens através da API de Apresentação.

### 2. Backend (Django)

**Descrição:**
O backend gerencia as requisições do frontend, interage com o servidor de imagens e gerencia os metadados associados às imagens. É responsável por servir os manifestos IIIF e garantir a conformidade com os padrões do IIIF.

**Tecnologias Utilizadas:**

- **Django:** Framework web em Python para desenvolvimento rápido e seguro do backend.

**Funcionalidades:**

- Gerenciamento de endpoints da IIIF API de Apresentação.
- Autenticação e autorização de usuários para o gerenciamento de imagens.
- Integração com o servidor de imagens e o banco de dados.

### 3. Servidor de Imagens

**Descrição:**
O servidor de imagens é responsável pelo armazenamento e fornecimento eficiente das imagens em alta qualidade. Utiliza o **Cantaloupe** como servidor de imagens IIIF, que suporta a entrega de imagens em múltiplas resoluções e formatos.

**Tecnologias Utilizadas:**

- **Cantaloupe:** Servidor de imagens que implementa a IIIF API de Imagem, permitindo o processamento e entrega de imagens dinâmicas.

**Funcionalidades:**

- Redimensionamento e formatação dinâmica de imagens sob demanda.
- Cache de imagens para melhorar a performance e reduzir a carga no servidor.
- Suporte a múltiplos formatos de imagem (TIF, JPEG, PNG, etc.).

### 4. Gerenciamento de Metadados

**Descrição:**
Os metadados associados às imagens são gerenciados pelo backend para fornecer contexto adicional e facilitar a busca e a organização das imagens dentro do sistema.

**Tecnologias Utilizadas:**

- **MySQL:** Banco de dados relacional para armazenamento de metadados.
- **Django ORM:** Abstração para interagir com o banco de dados de forma eficiente e segura.

**Funcionalidades:**

- Armazenamento de informações como título, descrição, autor, data de criação, etc.
- Suporte a formatos de metadata gerais, é possível usar Dublin Core, Europeana ou qualquer outro padrão.

### 5. Banco de Dados

**Descrição:**
O banco de dados MySQL armazena todas as informações estruturadas necessárias para o funcionamento do sistema, incluindo metadados das imagens e dados de configuração do sistema.

**Tecnologias Utilizadas:**

- **MySQL:** Banco de dados relacional mais comum existente.

**Funcionalidades:**

- Armazenamento eficiente e seguro.
- Simplicidade e facilidade de integração com o Django ORM.

## Integração com IIIF

### API de Imagem

A **API de Imagem IIIF** é responsável por fornecer as imagens em diferentes resoluções e formatos conforme solicitado pelo frontend. O **Cantaloupe** atua como o servidor de imagens, processando as requisições e entregando as imagens de acordo com os parâmetros especificados na URL da API.

**Fluxo de Integração:**

1. O frontend solicita uma imagem através da IIIF Image API com parâmetros específicos (por exemplo, tamanho, formato).
2. O **Cantaloupe** processa a requisição, redimensiona a imagem conforme necessário e retorna a imagem ao frontend.
3. As imagens são armazenadas em um sistema de arquivos do servidor que é compartilhada com o **Django** para gerenciamento das imagens.

### API de Apresentação

A **API de Apresentação IIIF** define a estrutura dos manifestos que descrevem as imagens e seus metadados. O backend desenvolvido em **Django** serve esses manifestos, que são consumidos pelo frontend para renderizar as imagens e suas informações associadas.

**Fluxo de Integração:**

1. O frontend solicita um manifesto IIIF para uma imagem específica.
2. O backend Django gera o manifesto, incluindo URLs para a API de Imagem e metadados relevantes.
3. O frontend consome o manifesto e utiliza as informações para exibir a imagem e seus detalhes no Mirador.

## Fluxo de Interação

1. **Acesso:**
   - O usuário abre a aplicação frontend no navegador.
2. **Solicitação:**
   - O frontend solicita o manifesto IIIF da imagem desejada através da API de Apresentação.
3. **Geração do Manifesto:**
   - O backend Django processa a requisição, recupera os metadados da imagem do banco de dados e gera o manifesto IIIF correspondente.
4. **Entrega do Manifesto:**
   - O manifesto é enviado de volta ao frontend.
5. **Renderização:**
   - O frontend utiliza o manifesto para solicitar a imagem de alta qualidade via IIIF Image API.
   - O servidor de imagens (Cantaloupe) processa a requisição e retorna a imagem.
6. **Visualização:**
   - A imagem é exibida no Mirador.
