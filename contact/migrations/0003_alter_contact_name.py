# Generated by Django 5.0.7 on 2024-11-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Nama Lengkap'),
        ),
    ]
