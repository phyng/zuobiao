from django.contrib import admin
from dashboard.models import Question, Anser, User

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AnserAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_name', 'choice')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'sex', 'birthday', 'income', 'education', 'ip')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Anser, AnserAdmin)
admin.site.register(User, UserAdmin)
