# Generated by Django 3.2.8 on 2022-05-12 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogIn_SignUp', '0003_auto_20220511_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_video_color',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
