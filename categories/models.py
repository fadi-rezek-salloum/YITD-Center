from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name_en = models.CharField(max_length=75, unique=True)
    name_ar = models.CharField(max_length=75, unique=True)

    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"{self.name_en} | {self.name_ar}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

        return super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    