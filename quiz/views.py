from django.shortcuts import render
from django.http import HttpResponse

def quiz_home(request):
    return HttpResponse("Quiz Home")


def quiz_view(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        score = 0
        for question in quiz.questions.all():
            answer = request.POST[f'question-{question.id}']
            if answer == question.correct_answer:
                score += 1
        return render(request, template_name="quiz/result.html", context={'quiz': quiz, 'score': score})
    else:
        return render(request, template_name="quiz/result.html", context={'quiz': quiz})