from django import forms
from crm import models


class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = models.School
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        # 在父类的初始化方法中将7个字段当成字典放到了 self.fields 中。
        super(SchoolModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    