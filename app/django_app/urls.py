from django.urls import path
from .  import views

urlpatterns = [
    path('<int:id>/<name>/', views.SampleCreateView.as_view(), name='create'),
    path('next<int:id>/<name>', views.NextView.as_view(), name='next'),
]
