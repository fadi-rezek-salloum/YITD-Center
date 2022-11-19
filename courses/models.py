from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from categories.models import Category

DIFFICULTY_CHOICES = (
    ('b', _('Beginner')),
    ('i', _('Intermediate')),
    ('e', _('Expert'))
)

class Course(models.Model):
    name_en = models.CharField(max_length=100, unique=True)
    name_ar = models.CharField(max_length=100, unique=True)

    description_en = models.TextField(null=True, blank=True)
    description_ar = models.TextField(null=True, blank=True)

    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, max_length=13)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    thumbnail = models.ImageField(upload_to="courses/")

    featured = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_en} | {self.name_ar}"

    def get_absolute_url(self):
        return reverse("course:course_details", kwargs={"pk": self.pk})    
    
    class Meta:
        ordering = ('-created',)