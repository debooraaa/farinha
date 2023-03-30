# Generated by Django 4.1.4 on 2023-03-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=100)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descrição', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
