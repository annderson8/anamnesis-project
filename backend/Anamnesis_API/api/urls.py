from django.urls import path
from .views import QuestionView

urlpatterns = [
    path('questions/', QuestionView.as_view(), name='questions_list' ),
    path('questions/<int:id>', QuestionView.as_view(), name='questions_process' )
]
