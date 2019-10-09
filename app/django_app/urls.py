from django.urls import path
from .  import views

urlpatterns = [
    path('<int:id>/<name>/', views.IndexView.as_view(), name='index'),
    path('next<int:id>/<name>', views.NextView.as_view(), name='next'),
]
