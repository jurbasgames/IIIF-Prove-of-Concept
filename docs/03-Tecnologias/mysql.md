# Banco de Dados MySQL

Para o armazenamento das estruturas IIIF e metadados, foi utilizado o **SGBD MySQL**, devido à sua popularidade e facilidade de integração com o framework **Django**. Em vez de interagir diretamente com o MySQL, utilizamos o **Django ORM** (Object-Relational Mapping), que permite a criação e manipulação de modelos em Python.

## Visão Geral

O **MySQL** é um sistema de gerenciamento de banco de dados relacional (SGBD) amplamente utilizado em aplicações web. Sua integração com o Django, através do Django ORM, facilita o desenvolvimento rápido.

## Modelos e Migrações

### Utilização do Django ORM

O Django ORM permite a definição de modelos em Python, que são automaticamente traduzidos em tabelas no MySQL durante as migrações. Isso facilita a criação e manipulação de dados no banco de dados, sem a necessidade de escrever SQL manualmente. Segue um exemplo de modelo:

```python
class Image(models.Model):
    format = models.CharField(max_length=50, db_index=True, blank=True)
    height = models.IntegerField(validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    width = models.IntegerField(validators=[MinValueValidator(1)], editable=False, null=True, blank=True)
    file = models.FileField()
```

As migrações são usadas para registrar as alterações dos modelos no banco de dados. Sempre que um modelo é criado ou modificado, é necessário gerar e aplicar migrações para alterar as mudanças nas tabelas do banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```
