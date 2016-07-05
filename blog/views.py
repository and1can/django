from django.shortcuts import render, get_object_or_404, redirect
from .models import Post # import to allow posts in database to display
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'django/post_list.html', {'posts': posts}) #posts is a variable that can 
																	  #be used in templates
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'django/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm() #creates form object that has a post, text, and title
    return render(request, 'django/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'django/post_edit.html', {'form': form})