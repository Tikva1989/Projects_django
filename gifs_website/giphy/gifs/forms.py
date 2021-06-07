from django import forms
# from django.forms.widgets import SelectMultiple
from .models import Category, Gif, Uploader
from django.core.files.uploadedfile import SimpleUploadedFile


# class GifForm(forms.ModelForm):
#     class Meta:
#         model = Gif
#         fields = '__all__'
#         widgets = {'categories': SelectMultiple}
        

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields= ['name'] 
#         labels = {'name': Category.name}

class GifForm(forms.Form):
    uploader_name=forms.CharField(max_length=40)
    title=forms.CharField(max_length=100)
    url=forms.CharField(max_length=200)
    categories=forms.ModelMultipleChoiceField(queryset=Category.objects.all())

   
   
class CategoryForm(forms.Form):
    name=forms.CharField(max_length=40)


class UploaderForm(forms.Form):
    img = forms.ImageField()
    name= forms.CharField(max_length=40)
# file_data= {'img': SimpleUploadedFile('test.png', <file data>)}
# form = UploaderForm({}, file_data)



