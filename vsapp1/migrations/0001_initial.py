# Generated by Django 2.2.4 on 2019-08-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.TextField()),
                ('gender', models.ImageField(upload_to='')),
                ('fav', models.IntegerField()),
                ('degree', models.IntegerField()),
                ('played', models.IntegerField()),
                ('won', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('gender', models.IntegerField()),
                ('fav', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('degree', models.IntegerField()),
                ('played', models.IntegerField()),
                ('won', models.IntegerField()),
            ],
        ),
    ]
