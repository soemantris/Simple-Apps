# Generated by Django 5.0.7 on 2024-08-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]