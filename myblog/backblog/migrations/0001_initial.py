# Generated by Django 2.1.4 on 2019-01-15 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=15)),
                ('describe', models.CharField(max_length=150)),
                ('tags', models.CharField(max_length=20)),
                ('titlepic', models.ImageField(upload_to='upload')),
                ('visibility', models.BooleanField(default=0)),
                ('crate_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Backblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('userpwd', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'tb_backblog',
            },
        ),
        migrations.CreateModel(
            name='BackblogToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=20)),
                ('backblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backblog.Backblog')),
            ],
            options={
                'db_table': 'tb_backblog_token',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('alias', models.CharField(max_length=20)),
                ('keywords', models.CharField(max_length=10)),
                ('describe', models.CharField(max_length=200)),
                ('fid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backblog.Category')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=10)),
                ('p_content', models.ImageField(upload_to='upload')),
            ],
            options={
                'db_table': 'picture',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backblog.Category'),
        ),
    ]
