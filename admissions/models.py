from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from  embed_video.fields  import  EmbedVideoField

class Admission(models.Model):
    title_ar = models.CharField(max_length=200, unique=True)
    title_en = models.CharField(max_length=200, unique= True)

    description_ar = models.TextField()
    description_en = models.TextField()

    slug = models.SlugField(blank=True, unique=True)

    thumbnail = models.ImageField(upload_to='admissions/')

    video = EmbedVideoField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title_en)

        return super().save()

    def get_absolute_url(self):
        return reverse("admissions:admission-details", kwargs={"slug": self.slug})
    

    class Meta:
        ordering = ('-created',)