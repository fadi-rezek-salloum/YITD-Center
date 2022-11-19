from django.views import generic

from .models import Admission

class AdmissionsList(generic.ListView):
    model = Admission
    context_object_name = 'admissions'
    template_name = 'admissions/list.html'


class AdmissionDetails(generic.DetailView):
    model = Admission
    context_object_name = 'admission'
    template_name = 'admissions/details.html'