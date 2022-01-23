from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from manager.managers import PersonManager
# Create your models here.

class Person(AbstractBaseUser):  #1
    objects = PersonManager()  # 2

    identifier = models.CharField(max_length=64, unique=True, blank=False)  # 3
    name = models.CharField(max_length=128)
    email = models.EmailField()

    is_active = models.BooleanField(default=True)  # 必要です！

    USERNAME_FIELD = 'identifier'  # 4

class Manager(models.Model):

    # 部署の定数
    DEP_ACCOUNTING = 0  # 経理
    DEP_SALES = 5  # 営業
    DEP_PRODUCTION = 10  # 製造
    DEP_DEVELOPMENT = 15  # 開発
    DEP_HR = 20  # 人事
    DEP_FIN = 25  # 財務
    DEP_AFFAIRS = 30  # 総務
    DEP_PLANNING = 35  # 企画
    DEP_BUSINESS = 40  # 業務
    DEP_DISTR = 45  # 流通
    DEP_IS = 50  # 情報システム

    # 人
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    # 部署
    department = models.IntegerField()
    # 着任時期
    joined_at = models.DateTimeField()
    # やめた時期
    quited_at = models.DateTimeField(null=True, blank=True)


class Worker(models.Model):

    # 人
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    # 着任時期
    joined_at = models.DateTimeField()
    # やめた時期
    quited_at = models.DateTimeField(null=True, blank=True)
    # 担当上司
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
