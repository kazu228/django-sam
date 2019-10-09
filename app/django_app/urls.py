from django.urls import path
from .  import views

urlpatterns = [
    path('<int:id>/<name>/', views.IndexView.as_view(), name='index'),
]
