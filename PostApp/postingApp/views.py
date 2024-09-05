from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Posts
from .forms import Post_form
# Create your views here.


def make_a_post(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Post_form()
    return render(request, 'Post_Form.html', {'form': form})


def home_display(request):
    obj = Posts.objects.all()
    return render(request, 'home.html', {'data': obj})


def edit_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)  # Get the post by primary key

    if request.method == 'POST':
        form = Post_form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Post_form(instance=post)

    return render(request, 'Post_Form.html', {'form': form})
