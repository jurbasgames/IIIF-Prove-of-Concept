# Generated by Django 5.0.7 on 2024-07-23 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('tipo', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('largura', models.IntegerField()),
                ('dimensoes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visualizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.IntegerField()),
                ('largura', models.IntegerField()),
                ('rotulo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Visualizações',
            },
        ),
        migrations.RemoveField(
            model_name='colecao',
            name='itens',
        ),
        migrations.AlterModelOptions(
            name='colecao',
            options={'verbose_name_plural': 'Coleções'},
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateField()),
                ('dimensoes', models.CharField(max_length=100)),
                ('localizacao_atual', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(max_length=50)),
                ('imagem_arquivo', models.ImageField(blank=True, null=True, upload_to='imagens/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objetos', to='app.categoria')),
            ],
            options={
                'verbose_name_plural': 'Objetos',
            },
        ),
        migrations.AddField(
            model_name='colecao',
            name='objetos',
            field=models.ManyToManyField(related_name='colecoes', to='app.objeto'),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
