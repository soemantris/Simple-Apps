from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug_cat = models.SlugField(blank=True)
    icons = models.ImageField(
        blank=True, default='category.png', upload_to='media/category')

    def save(self, *args, **kwargs):
        self.slug_cat = slugify(self.title)
        return super(Artcile, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Artcile(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    fill = models.TextField()
    images = models.ImageField(
        blank=True, default='articles.jpg', upload_to='media/articles')
    slug = models.SlugField(blank=True, editable=False)
    # tags
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Artcile, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
