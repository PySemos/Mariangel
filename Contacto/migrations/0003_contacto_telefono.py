# Generated by Django 3.2.8 on 2022-05-09 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0002_contacto_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
