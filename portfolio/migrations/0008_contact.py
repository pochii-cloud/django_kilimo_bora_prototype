# Generated by Django 3.1.7 on 2021-04-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_enquire_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
