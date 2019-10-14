from django import forms
from .models import Sample
from django.contrib.auth.forms import (
    AuthenticationForm
)

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['name', 'mail', 'age']

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        word_list = ['メールアドレス', 'パスワード']
        i = 0   #インスタンスとして利用しないのでselfをつけていないが文法的に問題があるのか、ないのか？
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.label = word_list[i]
            i += 1