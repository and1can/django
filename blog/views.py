from django.shortcuts import render
from .models import Post # import to allow posts in database to display
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'django/post_list.html', {'posts': posts}) #posts is a variable that can 
																	  #be used in templates