# Generated by Django 5.0.7 on 2024-08-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
