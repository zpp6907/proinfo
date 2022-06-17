from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题', max_length=32)
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=2)
    creat_time = models.DateTimeField(verbose_name='创建时间')

    # 级联删除
    depart = models.ForeignKey(verbose_name='部门',to="Department", to_field="id", on_delete=models.CASCADE)

    # 清空
    # depart = models.ForeignKey(to="Department", to_fields="id", null = True , blank= True, on_delete=models.SET_NULL)

    gender_choices = (
        (1, "男"),
        (2, "女")
    )

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
