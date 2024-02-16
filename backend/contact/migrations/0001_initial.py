# Generated by Django 5.0.1 on 2024-01-31 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('foto', models.ImageField(upload_to='foto_contato')),
            ],
        ),
    ]