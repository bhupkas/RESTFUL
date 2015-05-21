from django.conf.urls import url
from restful import views

urlpatterns = [
    url(r'^profiles/$', views.profile_list),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.profile_detail),
]
