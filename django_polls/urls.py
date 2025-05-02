from django.urls import path
from django_polls import views

app_name = 'django_polls'
urlpatterns = [
    # ex: /django_polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /django_polls/5
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    # ex: /django_polls/5/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /django_polls/5/vote
    path("<int:question_id>/vote", views.vote, name="vote")
]
