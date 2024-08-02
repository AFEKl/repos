# Generated by Django 5.0.7 on 2024-07-31 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_alter_video_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='embed',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]