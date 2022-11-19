import datetime

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail

from .models import Course

class CourseDetails(generic.DetailView):
    model = Course
    template_name = "courses/details.html"


class RequestCourse(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):

        course = get_object_or_404(Course, pk=kwargs['pk'])

        subject = f"Request to get: {course.name_en}"
        message = f"User: {request.user.first_name} {request.user.last_name} <br><br> Email: {request.user.email} <br><br> Phone: {request.user.phone} <br><br> Address: {request.user.address} <br><br> Requested course {course.name_en} on {datetime.datetime.now()}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER,]
        send_mail(subject=subject, message=None, from_email=from_email, recipient_list=recipient_list, html_message=message)
        
        return HttpResponseRedirect(f'/course/details/{kwargs["pk"]}')