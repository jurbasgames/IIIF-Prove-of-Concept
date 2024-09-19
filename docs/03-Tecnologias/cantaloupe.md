# Servidor de Imagens Cantaloupe

O Cantaloupe é um servidor de imagens de código aberto que implementa a API de Imagem do IIIF. Ele é uma ótima escolha pela sua capacidade de servir imagens em alta qualidade e escalabilidade, além de ser extremamente fácil de configurar e manter.

Na prova de conceito, utilizamos a imagem Docker `edirom/cantaloupe`, o que facilita ainda mais a configuração, sendo apenas necessário configurar o arquivo `cantaloupe.properties`.

## Visão Geral

- **Redimensionamento:** Serve imagens em diferentes resoluções.
- **Múltiplos formatos:** Compatível com diversos formatos de imagem, como JPEG, PNG, TIFF, etc.
- **Diferentes opções de armazenamento:** Suporta armazenamento local e em nuvem como AWS S3, Azure Blob Storage e Google Cloud Storage.

## Instalação e Inicialização

### Usando Docker

1. Baixar a imagem Docker:

```bash
docker pull edirom/cantaloupe
```

2. Editar o arquivo de configurações `cantaloupe.properties`:

```txt
FilesystemSource.BasicLookupStrategy.path_prefix = /var/lib/cantaloupe/images/
```

3. (Opcional) Desativar a versão 2.0:

```txt
endpoint.iiif.2.enabled = false
endpoint.iiif.3.enabled = true
```

4. Caso deseje iniciar apenas o Cantaloupe:

```bash
docker run -d -p 8182:8182 -v ./cantaloupe/cantaloupe.properties:/etc/cantaloupe.properties edirom/cantaloupe
```

# Referências

- [Site oficial](https://cantaloupe-project.github.io/)
- [Repositório GitHub](https://github.com/cantaloupe-project/cantaloupe)
- [Imagem Docker do Cantaloupe](https://hub.docker.com/r/edirom/cantaloupe)
