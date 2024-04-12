# Generated by Django 5.0 on 2024-03-08 20:03

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_category_signin'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='signin',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='signin',
            old_name='Username',
            new_name='username',
        ),
        migrations.AddField(
            model_name='signin',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
