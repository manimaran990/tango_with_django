from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from .models import Todo

# Create your views here.
@login_required(login_url='login')
def todo(request):
	if not request.user.is_authenticated:
		return render(request, "todo/login.html", {"message": None})

	context = {
		"items": Todo.objects.filter(author=request.user),
		"user": request.user
	}
	return render(request, 'todo/todo.html', context);

# @login_required(login_url='/todo/login/')
def addtodo(request):
	if not request.user.is_authenticated:
		return render(request, "todo/login.html", {"message": None})

	item = request.POST['todoitem']
	t = Todo(task=item, author=request.user)
	t.save()
	return HttpResponseRedirect(reverse('todo'))

# @login_required(login_url='/todo/login/')
def deletetodo(request, id):
	if not request.user.is_authenticated:
		return render(request, "todo/login.html", {"message": None})

	t = Todo.objects.get(pk=id)
	t.delete()
	return HttpResponseRedirect(reverse('todo'))


def login_view(request):
	username = request.POST.get("username", "Guest")
	password = request.POST.get("password", "guest")
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("todo"))
	else:
		return render(request, "todo/login.html", {"message": None})

def logout_view(request):
	logout(request)
	return render(request, "todo/login.html", {"message": "logged out!"})
