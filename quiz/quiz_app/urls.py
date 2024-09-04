from django.urls import path
# from .views import (
   
# )
from quiz_app import views
app_name = 'quiz_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('quiz/<int:question_index>', views.display_question, name = 'display_question'),
    path('submit/<int:question_index>', views.submit_answer, name = 'submit_answer'),        
]

