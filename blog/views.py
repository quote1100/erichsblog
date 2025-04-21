from django.shortcuts import render
from .models import Posts
from multiprocessing import context
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'about me'})

def posts(request):
    context = {
        'title': 'Personal Posts',
        'personalposts' : personalposts
    }
    return render(request, 'blog/posts.html', context)

class PostListView(ListView):
    model = Posts
    template_name = 'blog/posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'personalposts'
    ordering = ['-created_at']
    paginate_by = 1

class PostDetailView(DetailView):
    model = Posts

class PostCreateView (CreateView):
    model = Posts
    fileds = ['title','content']
 
def rpcoff(request):
    return render(request, 'blog/rpcoff.html', {'title': 'Rock Paper Scissors Java version'})

def fp1(request):
    return render(request, 'blog/fp1.html', {'title': 'Under Construction'})

def fp2(request):
    return render(request, 'blog/fp2.html', {'title': 'Under Construction'})
