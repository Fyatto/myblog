from django.db import models


class Backblog(models.Model):
    username = models.CharField(max_length=10, unique=True)
    userpwd = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'tb_backblog'


class BackblogToken(models.Model):
    backblog = models.ForeignKey(Backblog, on_delete=models.CASCADE)
    token = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_backblog_token'


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    keywords = models.CharField(max_length=15)
    describe = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.CharField(max_length=20)
    titlepic = models.ImageField(upload_to='upload')
    visibility = models.BooleanField(default=0)
    crate_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'


class Category(models.Model):
    name =models.CharField(max_length=10, unique=True)
    alias = models.CharField(max_length=20)
    fid = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    keywords = models.CharField(max_length=10)
    describe = models.CharField(max_length=200)

    class Meta:
        db_table = 'category'

class Picture(models.Model):
    p_name = models.CharField(max_length=10)
    p_content = models.ImageField(upload_to='upload')

    class Meta:
        db_table = 'picture'


