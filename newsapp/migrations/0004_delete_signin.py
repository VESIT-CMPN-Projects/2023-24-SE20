# Generated by Django 5.0 on 2024-03-09 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_alter_signin_managers_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='signin',
        ),
    ]