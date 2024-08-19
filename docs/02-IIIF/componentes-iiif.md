# Componentes básicos do IIIF

## Manifest (Manifesto)

O manifesto é a principal estrutura do padrão IIIF, cada manifesto representa geralmente um objeto na vida real, como por exemplo uma pintura, fotografia, entrevista, um livro etc. Os manifestos são compostos por uma série de estruturas que descrevem aquele objeto, como por exemplo, a sequência de imagens que compõem um livro, a transcrição de um texto, a localização de um objeto em um mapa, etc.

A principal estrutura que todo manifesto deve ter são os _items_ que devem ser um ou mais _Canvas_.

## Canvas (Tela)

O _Canvas_ é uma estrutura que representa uma visualização de um objeto, como por exemplo uma página de um livro, uma imagem de uma pintura. Cada _Canvas_ pode ter uma ou mais imagens. As imagens são representadas por estruturas chamadas _Annotation_. Todo Canva deve ser associada a uma _Annotation_ pelo campo de `items`. As _Annotations_ são compostas por uma ou mais imagens e as _Annotations_ que não são definidas como _painting_ elas devem ser declaradas no campo de `annotations`, representando anotações textuais de fato.

## Annotation (Anotação)

A _Annotation_ pode representar uma imagem, um texto, um vídeo, um áudio, uma mídia em geral. Elas são compostas por um _Resource_ que irá declara qual é o tipo da midia e o conteúdo dela. As _Annotations_ são associadas a um _Canvas_ pelo campo de `target`.

## Content Resource (Conteúdo)

Os recursos geralmente são externos ao manifesto, como por exemplo uma imagem em um servidor de imagens como o Cantaloupe. Todo recurso deve ser referenciado a um _Canvas_, pois os Canvases representam uma visualização da mídia. Os recursos também podem ser textuais e declarados junto ao manifesto.
