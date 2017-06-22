from django.conf.urls import url
from . import views
app_name = 'courses'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addcourse$', views.addcourse, name='addcourse'),
    url(r'^modifycourse$', views.modifycourse, name='modifycourse'),
    url(r'^confirmdelete$', views.confirmdelete, name='confirmdelete'),
    url(r'^deletecourse$', views.deletecourse, name='deletecourse'),
    url(r'^commentcourse$', views.commentcourse, name='commentcourse'),
    url(r'^addcomment$', views.addcomment, name='addcomment'),
]