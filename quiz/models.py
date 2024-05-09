from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question= models.CharField(max_length= 500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer= models.CharField(max_length= 100)
    
    def __str__(self):
        return self.question
    
class Quiz(models.Model):
    title= models.CharField(max_length=500)
    questions = models.ManyToManyField(Question,related_name="quizzes")
    
    class Meta:
        verbose_name_plural ="Quizzes"

class UserQuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_attempts")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name="quiz_user")


class AttemptRecord(models.Model):
    attempt = models.ForeignKey(UserQuizAttempt, on_delete=models.CASCADE, related_name="attempt_record")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_record")
    answer = models.CharField(max_length=100)
    
    
    

    
