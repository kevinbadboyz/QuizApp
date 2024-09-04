from django.db import models

class Question(models.Model):
    name = models.TextField()
    option_a = models.CharField(max_length = 200)
    option_b = models.CharField(max_length = 200)
    option_c = models.CharField(max_length = 200)
    option_d = models.CharField(max_length = 200)
    correct_answer = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.name)
    
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, blank = True, null = True, on_delete = models.SET_NULL)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.answer) + ' - ' + str(self.question.correct_answer)

