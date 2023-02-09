from django.urls import path
from comment import views

app_name = 'comment'

urlpatterns = [
    path('add/comment/<int:product_id>/', views.CommentAddView.as_view(), name='add_comment'),
    path('add/question/<int:product_id>/', views.QuestionView.as_view(), name='add_question'),
]
