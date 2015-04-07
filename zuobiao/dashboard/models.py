# coding: utf-8

from django.db import models

SEX_CHOICES = (
    (1, '男'),
    (2, '女'),
)
INCOME_CHOICES = (
    (1, '0-25k'),
    (2, '25k-50k'),
    (3, '50k-75k'),
    (4, '75k-100k'),
    (5, '100k-150k'),
    (6, '150k-300k'),
    (7, '300k+')
)
EDU_CHOICES = (
    (1, '初中及以下'),
    (2, '高中'),
    (3, '大学'),
    (3, '研究生及以上'),
)
ANSER_CHOICES = (
    (1, '强烈反对'),
    (2, '反对'),
    (3, '同意'),
    (4, '强烈同意'),
)

class Question(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return str(self.name)
 
class User(models.Model):
    created = models.DateTimeField()
    sex = models.IntegerField('性别', choices=SEX_CHOICES)
    birthday = models.IntegerField('生日')
    income = models.IntegerField('年收入', choices=INCOME_CHOICES)
    education = models.IntegerField('学历', choices=EDU_CHOICES)
    ip = models.CharField(u'IP', max_length=32)
    
    country = models.CharField(u'IP所在国', max_length=512, null=True, blank=True)
    province = models.CharField(u'IP所在省', max_length=512, null=True, blank=True)
    city = models.CharField(u'IP所在市', max_length=512, null=True, blank=True)
    operators = models.CharField(u'IP所在运营商', max_length=512, null=True, blank=True)

    def __str__(self):
        return str(self.ip)

class Anser(models.Model):
    created = models.DateTimeField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    choice = models.IntegerField(u'答案', choices=ANSER_CHOICES)

    @property
    def question_name(self):
        return self.question.name 
    
    def __str__(self):
        return str(self.choice)