from django.conf.urls import url
from core import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^.*\.html', views.chapeudepalha_html, name='chapeudepalha'),

]