# Generated by Django 4.0.5 on 2022-06-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descript', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]