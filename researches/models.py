from django.db import models
from django.urls import reverse
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
        verbose_name_plural = 'Research Categories'


class Research(models.Model):
    name_en = models.CharField(max_length=200, unique=True)
    name_ar = models.CharField(max_length=200, unique=True)

    content_en = models.TextField(null=True, blank=True)
    content_ar = models.TextField(null=True, blank=True)
    
    slug = models.SlugField(blank=True, unique=True)

    file = models.FileField(upload_to='researches/', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_en} | {self.name_ar}"

    def get_absolute_url(self):
        return reverse("researches:research-details", kwargs={"slug": self.slug})    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

        return super(Research, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Scientific Researches'
