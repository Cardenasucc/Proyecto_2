# Generated by Django 5.0.3 on 2024-05-14 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inventario',
            new_name='Product',
        ),
    ]