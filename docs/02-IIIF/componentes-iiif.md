# Componentes Básicos do IIIF

No contexto desta prova de conceito, nem todos os componentes do IIIF foram implementados. Componentes como **Collection** foram deixados para implementações futuras, e a **Range** foi optada por não ser utilizada. Além disso, a **Sequence** não foi implementada, uma vez que é uma estrutura da versão 2.0 da API de Apresentação do IIIF, enquanto o foco deste projeto foi a versão 3.0.

## Visão Geral dos Componentes IIIF

- **Manifest**: Representa um objeto digital, como uma pintura, um manuscrito, fotografia ou livro.
- **Canvas**: Representa uma superfície onde as mídias são exibidas, como uma página de um livro.
- **Annotation**: Representa conteúdos associados a um Canvas, como imagens ou textos.
- **Annotation Page**: Agrupa múltiplas Annotations relacionadas a um Canvas, na prova de conceito usamos a relação um para um com _annotation_.
- **Content Resource**: Recursos referenciados pelas Annotations, como imagens armazenadas no servidor de imagem.

## Manifest (Manifesto)

O **Manifesto** é a principal estrutura do padrão IIIF. Cada manifesto representa geralmente um objeto no mundo real, como uma pintura, fotografia ou livro.

### Estrutura do Manifesto

- **@context**: Define o contexto JSON-LD para a interpretação correta dos dados.
- **id**: Identificador único do manifesto.
- **type**: Tipo do recurso, geralmente "Manifest".
- **label**: Título ou rótulo do manifesto.
- **items**: Lista de Canvases que compõem o manifesto.

## Canvas (Tela)

O **Canvas** é uma estrutura que representa uma visualização de um objeto, como uma página de um livro ou uma imagem de uma pintura. Cada Canvas pode conter uma ou mais Annotations que descrevem o conteúdo visualizado.

### Estrutura do Canvas

- **id**: Identificador único do Canvas.
- **type**: Tipo do recurso, geralmente "Canvas".
- **label**: Título ou rótulo do Canvas.
- **items**: Lista de Annotations associadas ao Canvas.

## Annotation (Anotação)

A **Annotation** representa um conteúdo associado a um Canvas. Pode ser uma imagem, texto, vídeo ou áudio. As Annotations são compostas por um **Resource** que declara o tipo de mídia e seu conteúdo. Elas são vinculadas a um Canvas por meio do campo `target`.

### Estrutura da Annotation

- **id**: Identificador único da Annotation.
- **type**: Tipo do recurso, geralmente "Annotation".
- **motivation**: Motivação ou propósito da Annotation ("painting", "commenting").
- **body**: O recurso associado, como uma imagem ou texto.
- **target**: Referência ao Canvas ao qual a Annotation está vinculada.

## Annotation Page (Página de Anotação)

A **Annotation Page** agrupa múltiplas, ou apenas uma, Annotations relacionadas a um Canvas específico.

### Estrutura da Annotation Page

- **id**: Identificador único da Annotation Page.
- **type**: Tipo do recurso, geralmente "AnnotationPage".
- **items**: Lista de Annotations contidas na página.

## Content Resource (Conteúdo)

Os **Content Resources** são recursos referenciados pelas Annotations, como imagens externas armazenadas em servidores de imagem (como o Cantaloupe), textos, vídeos ou outros tipos de mídia.

### Estrutura do Content Resource

- **id**: Identificador único do recurso.
- **type**: Tipo do recurso ("Image" ou "Text").
- **format**: Formato do recurso ("image/jpeg", "image/tif", "text/plain").
- **width** e **height**: Dimensões do recurso.

## Componentes Não Implementados

Durante o desenvolvimento da prova de conceito, alguns componentes do IIIF não foram implementados:

- **Collection**: Utilizado para agrupar múltiplos manifests. Será implementado em fases futuras para permitir a organização de coleções de objetos.
- **Range**: Facilita a navegação dentro de um manifesto, permitindo a criação de capítulos ou seções. Optou-se por não utilizar este componente na versão atual.
- **Sequence**: Estrutura da versão 2.0 da API de Apresentação, substituída pelas funcionalidades da versão 3.0.

## Diagrama dos Componentes IIIF

![Diagrama de Componentes IIIF](https://iiif.io/api/assets/images/data-model.png)
