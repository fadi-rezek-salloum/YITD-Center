from django.shortcuts import render, get_list_or_404

from .models import QuesModel
from courses.models import Course

def getQuiz(request, course_name_en):
    questions = get_list_or_404(QuesModel, course__name_en=course_name_en)
    course = Course.objects.get(name_en__icontains=course_name_en)
    course_name_ar = course.name_ar

    if request.method == 'POST':

        score=0
        percent = 0
        wrong=0
        correct=0
        total=0

        answers = {}

        for q in questions:
            total+=1
            if q.ans == request.POST.get(str(q.pk)):
                score+=10
                correct+=1
                answers[q.pk] = (request.POST.get(str(q.pk)), True)
            else:
                wrong+=1
                answers[q.pk] = (request.POST.get(str(q.pk)), False)

        percent = int(score/(total*10) *100)

        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'name_en': course_name_en,
            'name_ar': course_name_ar,
            'questions': questions,
            'answers': answers,
        }
        return render(request, 'quiz/list.html', context)

    else:
        context = {
            'name_en': course_name_en,
            'questions': questions
        }

    return render(request, "quiz/list.html", context)