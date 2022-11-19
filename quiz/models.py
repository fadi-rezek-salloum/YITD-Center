from django.db import models
from django.utils.translation import gettext_lazy as _

from courses.models import Course

class QuesModel(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    question = models.CharField(max_length=200)

    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)

    ans = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question    

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")