from django.conf.urls import url
from userdetail import views

#Forming URLs
urlpatterns = [
    url(r'^$', views.userdata_retrieval, name='userdetail'),
]
