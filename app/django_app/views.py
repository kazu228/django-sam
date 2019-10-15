from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import SampleForm, LoginForm
from .models import Sample
from django.template import RequestContext
import datetime
from django.contrib.auth import get_user_model
from .forms import UserCreateForm

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
   if request.method =='GET':
       MyLoginForm = LoginForm()

   if MyLoginForm.is_valid():
        username = MyLoginForm.cleaned_data['username']
   else:
        MyLoginForm = LoginForm()
   
   response = render_to_response(request, 'loggedin.html', {"username" : username}, context_instance = RequestContext(request))
   
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

#     return render(request, 'django_app/index.html', params


User = get_user_model()

class UserList(generic.ListView):
    """ユーザーを一覧表示。"""
    # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に指定する。
    template_name = 'app/user_list.html'
    model = User

def user_data_input(request):
    """新規ユーザー情報の入力。"""
    # 一覧表示からの遷移や、確認画面から戻るリンクを押したときはここ。
    if request.method == 'GET':
        # セッションに入力途中のデータがあればそれを使う。
        form = UserCreateForm(request.session.get('form_data'))
    else:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            # 入力後の送信ボタンでここ。セッションに入力データを格納する。
            request.session['form_data'] = request.POST
            return redirect('app:user_data_confirm')

    context = {
        'form': form
    }
    return render(request, 'app/user_data_input.html', context)

def user_data_confirm(request):
    """入力データの確認画面。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('app:user_data_input')

    context = {
        'form': UserCreateForm(session_form_data)
    }
    return render(request, 'app/user_data_confirm.html', context)

def user_data_create(request):
    """ユーザーを作成する。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    # ユーザー作成後は、セッションを空にしたいのでpopメソッドで取り出す。
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        # ここにはPOSTメソッドで、かつセッションに入力データがなかった場合だけ。
        # セッション切れや、不正なアクセス対策。
        return redirect('app:user_data_input')

    form = UserCreateForm(session_form_data)
    if form.is_valid():
        form.save()
        return redirect('app:user_list')

    # is_validに通過したデータだけセッションに格納しているので、ここ以降の処理は基本的には通らない。
    context = {
        'form': form
    }
    return render(request, 'app/user_data_input.html', context)
