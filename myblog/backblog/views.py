import random

from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from backblog.forms import CateForm
from backblog.models import Backblog, BackblogToken, Picture, Article, Category




# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'back/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        user = Backblog.objects.filter(username=username).first()
        # 校验密码
        # userpwd = make_password(userpwd)
        # if check_password(user.userpwd, userpwd):
        if user.userpwd == userpwd:
            res = HttpResponseRedirect(reverse('backblog:index'))
            s = '1234567dfhvbcvvcnnds'
            token = ''
            for i in range(20):
                token += random.choice(s)
            res.set_cookie('token', token, max_age=600000000)
            BackblogToken.objects.create(backblog_id=user.id, token=token)
            return res

        else:
            #登录不成功
            return HttpResponseRedirect(reverse('backblog:login'))


# 主页面
def index(request):
    if request.method == 'GET':
        token = request.COOKIES.get('token')
        if not token:
            return HttpResponseRedirect(reverse('backblog:login'))
        user_token = BackblogToken.objects.filter(token=token).first()
        if not user_token:
            return HttpResponseRedirect(reverse('backblog:login'))
        return render(request, 'back/index.html')


# 退出
def logout(request):
    if request.method == 'GET':
        res =HttpResponseRedirect(reverse('backblog:login'))
        # 删除cookies中的键值对
        res.delete_cookie('token')
        return res


# 回到后台
def background(request):
    if request.method == 'GET':
        res = HttpResponseRedirect(reverse('backblog:index'))
        request.COOKIES.get('token')
        return res

# 文章跳转,并实现分页操作
def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        tils = Article.objects.all()
        pg = Paginator(tils, 2)
        tils = pg.page(page)
        return render(request, 'back/article.html', {'tils': tils})

# 添加文章
@csrf_protect
def add_article(request):
    if request.method =='GET':
        Category_id = Category.objects.all()
        return render(request, 'back/add_article.html', {'Category_id': Category_id})
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        category_id = None if request.POST.get('category') == '' else int(request.POST.get('category'))
        tags = request.POST.get('tags')
        titlepic = request.POST.get('titlepic')
        Article.objects.create(title=title, content=content, keywords=keywords,
                               describe=describe, category_id=category_id, tags=tags,
                               titlepic=request.FILES.get('titlepic'))
        return HttpResponseRedirect(reverse('backblog:article'))


# 文章发布
@csrf_protect
def article_submit(request):
    if request.method == 'GET':
        articles2 = Article.objects.all()
        return render(request, 'back/article.html', {'articles1': articles2})




# 公告跳转


def notice(request):
    if request.method =='GET':
        return render(request, 'back/notice.html')

# 删除文章
# @csrf_protect
def del_article(request,id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backblog:article'))


# 更新/修改文章
@csrf_protect
def update_article(request,  id):
    if request.method == 'GET':
        # id = int(request.GET.get('id'))
        # if not id:
            # return None
        Category22 = Category.objects.all()
        up_article = Article.objects.filter(pk=id).first()
        return render(request, 'back/update_article.html', {'up_article': up_article, 'Category22': Category22})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        category_id = None if request.POST.get('category') == '' else int(request.POST.get('category'))
        tags = request.POST.get('tags')
        # titlepic = request.POST.get('titlepic')
        Article.objects.filter(pk=id).update(title=title, content=content, keywords=keywords,
                               describe=describe, category_id=category_id, tags=tags,
                               titlepic=request.FILES.get('titlepic'))
        # Article2 =Article.objects.all()
        return HttpResponseRedirect(reverse('backblog:article'))

        # up_article = Article.objects.all()
        # return HttpResponseRedirect(reverse('backblog:article'), {'up_article': up_article})



# 评论跳转
def comment(request):
    if request.method =='GET':
        return render(request, 'back/comment.html')


# 跳转栏目
@csrf_protect
def category(request):
    if request.method =='GET':
        Cate1 = Category.objects.all()
        return render(request, 'back/category.html', {'Cate1': Cate1})
    if request.method == 'POST':
        name =request.POST.get('name')
        alias =request.POST.get('alias')
        fid =request.POST.get('fid', None)
        keywords =request.POST.get('keywords')
        describe =request.POST.get('describe')
        if Category.objects.filter(name=name).exists():
            msg ='名字已存在'
            return render(request, 'back/category.html', {'msg': msg})
        # Category.objects.create(name=name, alias=alias, fid_id=None if int(fid) == 0 else int(fid),
        #                         keywords=keywords, describe=describe)
        Category.objects.create(name=name, alias=alias, fid_id=fid,
                                keywords=keywords, describe=describe)
        return HttpResponseRedirect(reverse('backblog:category'))


# 增加栏目
@csrf_protect
def add_category(request):
    if request.method == 'GET':
        Cate1 = Category.objects.all()
        return render(request, 'back/category.html', {'Cate1': Cate1})
    if request.method == 'POST':
        form =CateForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            fid = request.POST.get('fid')
            keywords = request.POST.get('keywords')
            describe = request.POST.get('describe')
            Category.objects.create(name=name, alias=alias, fid=fid, keywords=keywords, describe=describe )
            Cate2 = Category.objects.all()
            return render(request, 'back/category.html', {'Cate2': Cate2})
        else:
            errors = form.errors
            return render(request, 'back/category.html', {'errors': errors})


# 修改栏目
@csrf_protect
def update_category(request,id):
    if request.method == 'GET':
        update_category1 = Category.objects.filter(pk=id).first()
        return render(request, 'back/update_category.html', {'update_category1': update_category1})
    if request.method == 'POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        fid = request.POST.get('fid', None)
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        Category.objects.filter(pk=id).update(name=name, alias=alias, fid=fid, keywords=keywords, describe=describe)
        return HttpResponseRedirect(reverse('backblog:category'))





# 跳转其他
def flink(request):
    if request.method =='GET':
        return render(request, 'back/flink.html')


# 跳转用户/访问记录
def loginlog(request):
    if request.method =='GET':
        return render(request, 'back/loginlog.html')


# 跳转管理用户
def manage_user(request):
    if request.method =='GET':
        return render(request, 'back/manage_user.html')


# 设置跳转
def setting(request):
    if request.method =='GET':
        return render(request, 'back/setting.html')


# 用户设置
def readset(request):
    if request.method =='GET':
        return render(request, 'back/readset.html')


# 实现编辑上传
def edit_article(request):
    """
    文章编辑方法
    """
    if request.method == 'GET':
        return render(request, 'back/add_article.html')
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 使用all()方法进行判断，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        if not all([title, content]):
            msg = '请填写完整的参数'
            return render(request, 'back/add_article.html', {'msg': msg})
        # 创建文章
        Article.objects.create(title=title,
                               content=content)
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('back/add_article.html'))


# 图片提交
@csrf_protect
def submit(request):
    if request.method =='GET':
        pass
    if request.method == 'POST':
        Picture.objects.create(p_name='haha',p_content=request.FILES.get('img'))
        return render(request, 'back/article.html')


# 删除栏目
@csrf_protect
def del_category(request, id):
    if request.method == 'GET':
        Category.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backblog:category'))








