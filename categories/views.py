from unicodedata import category
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Category

from courses.models import Course

class CategoryDetails(generic.ListView):

    model = Category
    allow_empty = False
    template_name = "categories/courses_list.html"

    def get(self, *args, **kwargs):
        self.slug = kwargs['slug']
        return super().get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['courses'] = Course.objects.filter(category__slug=self.slug)

        context['category_name'] = get_object_or_404(Category, slug=self.slug).name_en

        print(self.slug)

        return context