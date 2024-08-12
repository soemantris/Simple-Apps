from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    icons = models.ImageField(
        blank=True, default='category.png', upload_to='media/category')

    def __str__(self):
        return self.title


class Artcile(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    fill = models.TextField()
    images = models.ImageField(
        blank=True, default='articles.jpg', upload_to='media/articles')
    # tags
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
