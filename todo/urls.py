from django.urls import path

from . import views

urlpatterns = [
	path('', views.todo, name='todo'),
	path('add', views.addtodo, name='addtodo'),
	path('delete/<int:id>', views.deletetodo, name='deletetodo'),
	path('login', views.login_view, name='login'),
	path('logout', views.logout_view, name='logout')
]