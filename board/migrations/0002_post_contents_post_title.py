# Generated by Django 4.0.5 on 2022-06-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contents',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]