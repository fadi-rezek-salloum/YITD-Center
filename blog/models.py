from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from categories.models import Category


class SubCategory(models.Model):
    name_en = models.CharField(max_length=75, unique=True)
    name_ar = models.CharField(max_length=75, unique=True)

    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"{self.name_en} | {self.name_ar}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

        return super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Medical Sub Categories'


class Post(models.Model):
    title_ar = models.CharField(max_length=255, unique=True)
    title_en = models.CharField(max_length=255, unique=True)

    content_ar = RichTextField()
    content_en = RichTextField()

    thumbnail = models.ImageField(upload_to='blog/')

    slug = models.SlugField(blank=True, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, help_text='If this post is medical, please select a sub-category')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("blog:post-details", kwargs={"slug": self.slug})

    def save(self):

        if not self.slug:
            self.slug = slugify(self.title_en)

        return super().save()
    

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    first_name = models.CharField(_('First Name'), max_length=55)
    last_name = models.CharField(_('Last Name'), max_length=55)

    email = models.EmailField(_('Email Address'), unique=True)

    comment = models.TextField()

    def __str__(self):
        return 'Comment From: ' + self.first_name + ' ' + self.last_name
    