
from django import forms

from backblog.models import Category


class CateForm(forms.Form):
    name =forms.CharField(max_length=10,
                          min_length=2,
                          required=True,
                          error_messages={
                              'required': '栏目名称必填',
                              'max_length': '不能超过10字符',
                              'min_length': '不能少于2字符'
                          })
    alias =forms.CharField(max_length=10,
                          min_length=2,
                          required=True,
                          error_messages={
                              'required': '栏目别名必填',
                              'max_length': '不能超过10字符',
                              'min_length': '不能少于2字符'
                          })




    def clean_name(self):
        # 校验栏目名称
        name = self.cleaned_data.get('name')
        cate =Category.objects.filter(name=name).first()
        if cate:
            raise forms.ValidationError('栏目名称重复')
        return self.cleaned_data['name']