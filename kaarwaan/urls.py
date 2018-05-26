from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'kaarwaan'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='kaarwaan/index.html'), name='index'),
    url(r'^Data/$', views.data, name='data'),
    url(r'^Data/students/$', views.school_detail, name='students'),
    url(r'^Data/students/marks/$', views.result, name='result'),
]