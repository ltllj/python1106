from django.conf.urls import url

from user.views import reg, login

urlpatterns = [
    url(r'^reg/$', reg, name='注册'),
    url(r'^login/$', login, name='登录'),
]
