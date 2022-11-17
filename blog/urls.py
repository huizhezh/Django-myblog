from django.urls import re_path

from blog.views import post_pk, archive

urlpatterns =[
    re_path(r'^$', archive),
    re_path(r'^(?P<pk>[0-9]+)/$', post_pk),

]
