from django.urls import path, url
from .  import views
app_name = 'django_app'
urlpatterns = [
    path('', views.SampleCreateView.as_view(), name='create'),
    path('next', views.NextView.as_view(), name='next'),
    url(r'^connection/','formView', name = 'loginform'),
    url(r'^login/', 'login', name = 'login')
]
