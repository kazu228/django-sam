from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'django_app/index.html'
    
class NextView(generic.TemplateView):
    template_name = 'django_app/next.html'   

class SampleCreateView(generic.CreateView):
    from_class = SampleForm
    template_name = 'django_index.html'

# def index(request, id, name):
#     params = {
#         'id': id,
#         'name': name,
#     }
#     result = 'あなたのidは' + str(id) + 'あなたの名前は' + name + "です。"

#     return render(request, 'django_app/index.html', params)