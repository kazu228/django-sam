from django.urls import path
from .  import views
from django.conf.urls import url
app_name = 'django_app'
urlpatterns = [
    path('', views.SampleCreateView.as_view(), name='create'),
    path('next', views.NextView.as_view(), name='next'),
    url(r'^connection/',views.formView, name = 'loginform'),
    url(r'^login/', views.login, name = 'login')
]
