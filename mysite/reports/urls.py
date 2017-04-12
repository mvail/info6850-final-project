from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /patent/5/
    url(r'^(?P<pid>[0-9]+)/$', views.detail, name='detail'),
    url(r'^datatables/$', views.datatables, name='datatables'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^keywords/$', views.keywords, name='keywords'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^complex/$', views.complex, name='complex'),
]