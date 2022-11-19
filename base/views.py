from django.views import generic

from courses.models import Course

class Index(generic.ListView):
    model = Course
    context_object_name = "courses"
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['courses'] = Course.objects.filter(featured=True)

        return context


class About(generic.TemplateView):
    template_name = "base/about.html"