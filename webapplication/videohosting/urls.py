from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url
from .views import CreatePost, GetDistraction
from .views import LoadPost
from .views import ReceiveDistraction

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^createPost', CreatePost.as_view()),
    url(r'^loadPost', LoadPost.as_view()),
    url(r'^receiveDistraction', ReceiveDistraction.as_view()),
    url(r'^getDistraction', GetDistraction.as_view()),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    url(r'', LoadPost.as_view()),
    url(r'', LoadPost.as_view(), name='home'),

    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
