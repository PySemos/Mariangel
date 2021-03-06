# Generated by Django 3.2.8 on 2022-05-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Nombre de usuario')),
                ('last_name', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Apellido paterno')),
                ('password', models.CharField(max_length=40, verbose_name='Contraseña')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('age', models.IntegerField(blank=True, default=0, null=True, verbose_name='Edad')),
                ('ci', models.CharField(default='', max_length=30)),
                ('ip_address', models.CharField(default='', max_length=20)),
                ('is_logged', models.BooleanField(default=False)),
                ('last_login', models.BooleanField(default=False)),
                ('last_video_color', models.CharField(default='', max_length=30)),
                ('last_video_abc', models.CharField(default='', max_length=30)),
                ('last_video_simple_phrases', models.CharField(default='', max_length=30)),
                ('last_video_simple_words', models.CharField(default='', max_length=30)),
                ('has_been_tested', models.BooleanField()),
            ],
        ),
    ]
