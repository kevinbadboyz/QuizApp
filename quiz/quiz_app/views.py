from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Question
from .forms import UserAnswerForm

def index(request, template_name = 'index/index.html'):
    title = 'QuizApp'
    button = 'Start Quiz'
    context = {
        'title' : title,
        'button' : button,
    }
    return render(request, template_name, context)

def display_question(request, question_index, template_name = 'index/question.html'):
    total_questions = Question.objects.count()    
    question = Question.objects.all()[question_index]
    print('Question Index DQ : ' + str(question_index))    

    context = {
        'question' : question,
        'question_index' : question_index,
        'total_questions' : total_questions,
    }
    return render(request, template_name, context)

def submit_answer(request, question_index, template_name = 'index/question.html'):
    question = Question.objects.all()[question_index]
    total = Question.objects.count()
    print('-------------Question index : ' + str(question_index))    
    form = UserAnswerForm(request.POST)
    if form.is_valid():
        user_answer = form.save(commit = False)        
        user_answer.question = Question.objects.get(id = question.id)
        user_answer.answer = form.cleaned_data.get('answer')
        user_answer.save()
        if (question_index < total - 1):
            print('Simpan dieksekusi')
            return redirect('quiz_app:display_question', question_index + 1) 
        else:
            print('Direct ke halaman index')
            return redirect('quiz_app:index') 
    context = {
        'form' : form,
    }
    return render(request, template_name, context)
