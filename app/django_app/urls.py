from django.urls import path
from .  import views
from django.conf.urls import url
app_name = 'django_app'
urlpatterns = [
    # path('', views.SampleCreateView.as_view(), name='create'),
    path('next', views.NextView.as_view(), name='next'),
    # url(r'^connection/',views.formView, name = 'loginform'),
    # url(r'^login/', views.login, name = 'login'),
    path('user_list', views.UserList.as_view(), name='user_list'),
    path('user_data_input/', views.user_data_input, name='user_data_input'),
    path('user_data_confirm/', views.user_data_confirm, name='user_data_confirm'),
    path('user_data_create/', views.user_data_create, name='user_data_create'),
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('add_cookie/', views.add_cookie),
    path('check_cookie', views.check_cookie),
]
