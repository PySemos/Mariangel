# Generated by Django 3.2.8 on 2022-05-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogIn_SignUp', '0004_alter_user_last_video_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='has_been_tested_abc',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_been_tested_simple_phrases',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_been_tested_simple_words',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_video_abc',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_video_color',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_video_simple_phrases',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_video_simple_words',
            field=models.IntegerField(default=1),
        ),
    ]