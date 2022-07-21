"""
@Time    : 2022/6/25 19:27
@Author  : peyzhang
@Email   : peyzhang@163.com
@File    : account.py.py
@Software: PyCharm
"""
from django.shortcuts import render
from django import forms
from app import models
from app.utils.encrypt import md5


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码")

# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = ["username", "password"]


    def clean_password(self):
        self.cleaned_data.get("password")

def login(request):
    """用户信息"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html',{"form" : form})

    form = LoginForm(data= request.POST)
    if form.is_valid():
        user_object = models.User.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password","用户名或密码错误")
            return render(request, 'login.html', {"form": form})



    return render(request, 'login.html', {"form": form})





def logon(request):
    """用户信息"""
    return render(request, 'logon.html')

