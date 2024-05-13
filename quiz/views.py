from django.shortcuts import render
from .models import Quiz, Question, AttemptRecord, UserQuizAttempt

def quiz_list_view(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/list.html', {'quizzes': quizzes})

def quiz_detail_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = quiz.questions.all()
    return render(request, 'quizzes/detail.html', {'quiz': quiz, 'questions': questions})

def take_quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = quiz.questions.all()
    if request.method == 'POST':
        # Process the user's answers
        answers = request.POST.getlist('answer')
        # Create an AttemptRecord for each question
        for i, question in enumerate(questions):
            answer = answers[i]
            AttemptRecord.objects.create(attempt=UserQuizAttempt.objects.create(user=request.user, quiz=quiz), question=question, answer=answer)
        return render(request, 'quizzes/results.html', {'quiz': quiz})
    return render(request, 'quizzes/take.html', {'quiz': quiz, 'questions': questions})