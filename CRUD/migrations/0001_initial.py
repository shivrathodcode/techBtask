# Generated by Django 5.0.2 on 2024-02-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
                ('captain', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('t_mem', models.IntegerField()),
            ],
        ),
    ]
