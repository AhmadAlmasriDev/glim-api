from django.urls import path
from commnets import views

urlpatterns =[
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetailS.as_view()),
]