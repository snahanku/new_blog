# Generated by Django 4.2.3 on 2023-11-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
    ]
