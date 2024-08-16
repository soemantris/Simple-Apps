# Generated by Django 5.0.7 on 2024-08-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artcile',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_cat',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='artcile',
            name='images',
            field=models.ImageField(blank=True, default='articles.jpg', upload_to='media/articles'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icons',
            field=models.ImageField(blank=True, default='category.png', upload_to='media/category'),
        ),
    ]