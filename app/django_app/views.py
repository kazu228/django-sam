from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import SampleForm, LoginForm
from .models import Sample
from django.template import RequestContext
import datetime
from django.contrib.auth import get_user_model
from .forms import UserCreateForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)

# Create your views here.


# class IndexView(generic.TemplateView):
#     template_name = 'django_app/index.html'

class SampleCreateView(generic.CreateView):
    form_class = SampleForm
    template_name = 'django_app/index.html'

class NextView(generic.ListView):
    model = Sample
    template_name = 'django_app/next.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'django_app/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'django_app/index.html'

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
    template_name = 'django_app/user_list.html'
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
            return redirect('django_app:user_data_confirm')

    context = {
        'form': form
    }
    return render(request, 'django_app/user_data_input.html', context)

def user_data_confirm(request):
    """入力データの確認画面。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('django_app:user_data_input')

    context = {
        'form': UserCreateForm(session_form_data)
    }
    return render(request, 'django_app/user_data_confirm.html', context)

def user_data_create(request):
    """ユーザーを作成する。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    # ユーザー作成後は、セッションを空にしたいのでpopメソッドで取り出す。
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        # ここにはPOSTメソッドで、かつセッションに入力データがなかった場合だけ。
        # セッション切れや、不正なアクセス対策。
        return redirect('django_app:user_data_input')

    form = UserCreateForm(session_form_data)
    if form.is_valid():
        form.save()
        return redirect('django_app:user_list')

    # is_validに通過したデータだけセッションに格納しているので、ここ以降の処理は基本的には通らない。
    context = {
        'form': form
    }
    return render(request, 'django_app/user_data_input.html', context)

def add_cookie(request):
    respsonse = HttpResponse("Cookie Test")
    respsonse.set_cookie("name", "john")
    return respsonse

def check_cookie(request):
    value = request.COOKIES["name"]
    return HttpResponse("Cookie test value %s" % value)

def post_comment(request):
    if request.method == 'POST':
        if request.session.get('has_commented', False):
            return HttpResponse("You've already commented")
        request.session['has_commented'] = True
        return HttpResponse('Thanks for your comment !!')
    return render_to_response('django_app/post_comment.html')