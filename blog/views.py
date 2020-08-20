from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Blog
from .forms import BlogForm

# Create your views here
def all(request):
	''' show all the blog post from all the users'''
	context = {
		"blogs": Blog.objects.all()
	}
	return render(request, 'blog/all.html', context)

@login_required(login_url='login')
def home(request):
	''' page to show user dashboard '''
	if request.method == 'POST':
		form = BlogForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('add_blog')

	context = {
		"blogs": Blog.objects.filter(user=request.user),
		"form": BlogForm()
	}
	return render(request, 'blog/home.html', context)


def view_blog(request, id):
	context = {
		"blog": Blog.objects.get(pk=id)
	}
	return render(request, 'blog/view.html', context)


def add_blog(request):
	''' view to add a blog post for the user '''
	title = request.POST['title']
	post = request.POST['post']
	blog = Blog(title=title, post=post, user=request.user)
	blog.save()

	return HttpResponseRedirect(reverse('home'))

def delete_blog(request, id):
	''' delete a blog by id '''
	blog = Blog.objects.get(pk=id)
	blog.delete()

	return HttpResponseRedirect(reverse('home'))

def update_blog(request, id):
	''' update a blog '''
	blogpost = Blog.objects.get(pk=id)
	form = BlogForm(instance=blogpost)

	if request.method == 'GET':
		form = BlogForm(request.POST, instance=blogpost)
		if form.is_valid(): 
			form.save() 
			return HttpResponseRedirect(reverse('home'))

	context = { "form": form } 
	return render(request, 'blog/update.html', context)

def login_view(request):
	'''login view'''
	username = request.POST.get('username', 'guest')
	password = request.POST.get('password', 'gpass')

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('home'))
	else:
		return render(request, 'blog/login.html', { 'message': 'invalid credentials!'})

def logout_view(request):
	''' logout view'''
	logout(request)
	return render(request, 'blog/login.html', { 'message': 'logged out!'})
