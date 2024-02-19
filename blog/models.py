from django.db import models
from django.utils.text import slugify


# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=128, null=False)
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog kategorya'
        verbose_name_plural = 'Blog kategoriyalari'


class BlogPost(models.Model):
    name = models.CharField(max_length=128, verbose_name="Maqola nomi", null=False)
    short_description = models.TextField(null=False, verbose_name="Maqola haqida qisqacha")
    description = models.TextField(null=False, verbose_name="Maqola haqida")
    category_id = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Maqola kategoryasi")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Maqola rasmi")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan sana")
    slug = models.SlugField(max_length=200, blank=True, unique=True, verbose_name='Slug', )

    view_count = models.ImageField(default=0, verbose_name="Ko'rishlar soni")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
