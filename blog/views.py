from django.shortcuts import render, get_object_or_404
from .models import Post # import to allow posts in database to display
from django.utils import timezone


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'django/post_list.html', {'posts': posts}) #posts is a variable that can 
																	  #be used in templates
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'django/post_detail.html', {'post': post})