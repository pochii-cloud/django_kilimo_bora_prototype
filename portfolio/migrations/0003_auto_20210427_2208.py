# Generated by Django 3.1.7 on 2021-04-27 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210427_2202'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Division',
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'verbose_name_plural': 'Divisions'},
        ),
    ]
