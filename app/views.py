from django.shortcuts import render
from app import models


# Create your views here.

def depart_list(request):
    """部门列表"""
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {'queryset': queryset})


def depart_delete(request):
    return


def depart_edit(request, nid):
    return


def user_list(request):
    return


from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "gender", "creat_time", "depart"]
        # widgets = {
        #     "name":forms.TextInput(attrs={"class": "form-control"})
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         field.widgets.attrs = {"class": "form-control"}


def user_add(request):
    """添加用户"""
    form = UserModelForm()
    return render(request, 'user_add.html', {"form": form})



