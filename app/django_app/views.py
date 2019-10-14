from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views import generic
from .forms import SampleForm, LoginForm
from .models import Sample
from django.template import RequestContext
import datetime

# Create your views here.


# class IndexView(generic.TemplateView):
#     template_name = 'django_app/index.html'

class SampleCreateView(generic.CreateView):
    form_class = SampleForm
    template_name = 'django_app/index.html'

class NextView(generic.ListView):
    model = Sample
    template_name = 'django_app/next.html'

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
   
   if MyLoginForm.is_valid():
      username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
   
   response = render_to_response(request, 'loggedin.html', {"username" : username}, 
      context_instance = RequestContext(request))
   
   response.set_cookie('last_connection', datetime.datetime.now())
   response.set_cookie('username', datetime.datetime.now())
	
   return response

def formView(request):
   if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
         "%Y-%m-%d %H:%M:%S")
      
      if (datetime.datetime.now() - last_connection_time).seconds < 10:
         return render(request, 'loggedin.html', {"username" : username})
      else:
         return render(request, 'login.html', {})
			
   else:
      return render(request, 'login.html', {})
# def index(request, id, name):
#     params = {
#         'id': id,
#         'name': name,
#     }
#     result = 'あなたのidは' + str(id) + 'あなたの名前は' + name + "です。"

#     return render(request, 'django_app/index.html', params)