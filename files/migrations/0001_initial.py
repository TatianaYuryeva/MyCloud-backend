# Generated by Django 4.2.5 on 2023-09-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('size', models.CharField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('download_last_date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('path', models.CharField()),
                ('download_link', models.CharField()),
                ('upload', models.FileField(upload_to='test')),
            ],
        ),
    ]
