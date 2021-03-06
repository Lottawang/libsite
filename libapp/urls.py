from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
        url(r'^suggestions/$', views.suggestions, name='suggestions'),
        url(r'^suggestionsdetails/(?P<item_id>\d+)$', views.suggestionsdetail, name='suggestionsdetail'),
        url(r'^searchlib/$', views.searchlib, name='searchitem'),
        url(r'^newitem/$', views.newitem, name='newitem'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^myitems/$', views.myitems, name='myitems'),
        url(r'^myitems/(?P<item_id>\d+)$', views.detail,name='myitemsdetails'),
        url(r'^register/$', views.register, name='register'),
        ]
