from django.urls import re_path, path

from article import views

urlpatterns = [
    # path函数将url映射到视图
    re_path('article-list/', views.article_list, name='article_list'),
    # 下面是分发路径的两种写法，都可以运行path和re_path，re_path正则匹配
    # re_path(r'^article-detail/(?P<id>[0-9]+)/$', views.article_detail, name='article_detail'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),

    path(
            'article-safe-delete/<int:id>/',
            views.article_safe_delete,
            name='article_safe_delete'
        ),

    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),

]
