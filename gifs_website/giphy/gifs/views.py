
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from .models import Category, Gif, Uploader
from .forms import CategoryForm, GifForm, UploaderForm
from django.views.generic import DetailView, TemplateView, View, CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin




def homepage(request):
    gifs= Gif.objects.all()
    return render(request, 'gifs/homepage.html', context={'gifs': gifs})


def add_category(request):
    if request.method=='GET':
        form=CategoryForm()
        return render(request,'gifs/add_category.html',{'form':form,'add_type':'Category'})

    if request.method=='POST':
        form =CategoryForm(request.POST)
        
        if form.is_valid():
            category=Category.objects.create(name=form.cleaned_data['name'])
        
        return redirect('homepage')


def add_gif(request):
  
    if request.method== 'GET':
        form = GifForm()
        return render(request, 'gifs/add_gif.html', {'form':form, 'add_type':'Gif'})
    #need to be fixed with no hard coded
    if request.method=='POST':
        form =GifForm(request.POST)
        if form.is_valid():
              Gif.objects.create(**form.cleaned_data)  
        return redirect('homepage')


class CategoryDetialView(DetailView):
    template_name= 'gifs/category_detail.html'
    context_object_name = 'category'
    model = Category
    fields = ['gifs', 'name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context


class AllCategoriesListView(ListView):
    template_name= 'gifs/all_categories.html'
    context_object_name = 'all_categories'
    model = Category
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GifDetialView(DetailView):
    template_name= 'gifs/single_gif.html'
    context_object_name = 'gif'
    model = Gif
    fields = '__all__'

#upload image using imageFields in forms

class UploaderCreateView(CreateView):
    model = Uploader
    fields = '__all__'
    
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['title']= 'Uploader Details'
        return context

   
    
    
         



    
