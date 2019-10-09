from django.urls import path
from .  import views

urlpatterns = [
    path('', views.SampleCreateView.as_view(), name='create'),
    path('next', views.NextView.as_view(), name='next'),
]
