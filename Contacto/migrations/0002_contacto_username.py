# Generated by Django 3.2.8 on 2022-05-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='username',
            field=models.CharField(default='', max_length=30, verbose_name='Nombre de Usuario'),
        ),
    ]
