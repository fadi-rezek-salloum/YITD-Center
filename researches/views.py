from django.views import generic

from .models import Category, Research

def list_research_categories(request):
    categories = Category.objects.all()

    return {
        'categories': categories
    }


class ResearchesList(generic.ListView):
    model = Research
    context_object_name = 'researches'
    template_name = 'researches/list.html'

    def get_queryset(self):
        return Research.objects.filter(category__name_en__icontains=self.kwargs['cat_name'])


class ResearchDetails(generic.DetailView):
    model = Research
    context_object_name = 'research'
    template_name = 'researches/details.html'