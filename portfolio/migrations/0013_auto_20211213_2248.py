# Generated by Django 3.1.7 on 2021-12-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20211213_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='response',
            field=models.CharField(default='Question not yet answered.check later', max_length=500),
        ),
    ]
