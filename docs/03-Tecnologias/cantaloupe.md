# Servidor de Imagens Cantaloupe

O Cantaloupe é um servidor de imagens de código aberto que implementa a API de Imagem do IIIF. Ele é uma ótima escolha pela sua capacidade de servir imagens em alta qualidade e escalabilidade, além de ser extremamente fácil de configurar e manter.

Na prova de conceito, usamos a imagem docker `edirom/cantaloupe` o que facilita ainda mais a configuração sendo apenas necessário configurar o arquivo `cantaloupe.properties`.

## Configuração

A configuração do Cantaloupe é feita através de um arquivo de propriedades chamado `cantaloupe.properties`. Esse arquivo contém uma grande quantidades de configurações, mas vamos focar nas mais importantes para o projeto.

### Configuração de Storage

O Cantaloupe suporta diversos tipos de storage, como o sistema de arquivos local que é o que usamos na prova de conceito, mas também suporta S3, Azure, Google Cloud.

```properties
FilesystemSource.BasicLookupStrategy.path_prefix = /var/lib/cantaloupe/images/
```

### Configuração de Versão do IIIF (Opcional)

Como o Cantaloupe suporta tanto a versão 2.0 quanto a 3.0 da API de Imagem do IIIF, é ativado por padrão o endpoint da versão 2.0. Podemos desativar isso.

```properties
endpoint.iiif.2.enabled = false
endpoint.iiif.3.enabled = true
```
