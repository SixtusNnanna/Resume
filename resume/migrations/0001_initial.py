# Generated by Django 4.1.2 on 2022-11-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=10)),
                ('end_year', models.CharField(max_length=10)),
                ('qulification', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('level', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(upload_to='pic/')),
                ('title', models.CharField(default='Chemical Engineer/ Fullstack Developer', max_length=100)),
                ('about', models.TextField(default='sixtus')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('level', models.PositiveIntegerField()),
            ],
        ),
    ]
