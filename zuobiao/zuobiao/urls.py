from django.conf.urls import patterns, include, url
from django.contrib import admin

from dashboard.views import QuestionApi

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zuobiao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/question/(?P<pk>\d+)/$', QuestionApi.as_view(), name='question_api'),
)
