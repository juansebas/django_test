# Generated by Django 2.2.7 on 2019-11-13 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]