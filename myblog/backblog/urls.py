from django.urls import path

from backblog import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('background/', views.background, name='background'),
    path('article/', views.article, name='article'),
    path('notice/', views.notice, name='notice'),
    path('comment/', views.comment, name='comment'),
    path('category/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('flink/', views.flink, name='flink'),
    path('loginlog/', views.loginlog, name='loginlog'),
    path('manage_user/', views.manage_user, name='manage_user'),
    path('setting/', views.setting, name='setting'),
    path('readset/', views.readset, name='readset'),
    path('add_article/', views.add_article, name='add_article'),
    # 文章发布
    path('article_submit/', views.article_submit, name='article_submit'),

    # 图片提交
    path('submit/', views.submit, name='submit'),

    # 删除文章
    path('del_article/<int:id>', views.del_article, name='del_article'),

    # 修改文章
    path('update_article/<int:id>/', views.update_article, name='update_article'),

    # 删除栏目
    path('del_category/<int:id>/', views.del_category, name='del_category'),

    # 修改栏目
    path('update_category/<int:id>/', views.update_category, name='update_category'),

    # 富文本操作
    # 编辑文章
    path(r'edit_article/', views.edit_article, name='edit_article'),
    # 文章列表
    path(r'article/', views.article, name='article'),




    # 查询所有title信息，实现分页操作
    # path('all_title/', views.all_title, name='all_title'),
    # 保存信息
    # path('add_title/', views.add_title, name='add_title'),



]