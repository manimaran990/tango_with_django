from django.urls import path

from . import views

urlpatterns = [
	path('', views.all, name='all'),
	path('home', views.home, name='home'),
	path('add', views.add_blog, name='add'),
	path('delete/<int:id>', views.delete_blog, name='deleteblog'),
	path('update/<int:id>', views.update_blog, name='updateblog'),
	path('view/<int:id>', views.view_blog, name='viewblog'),
	path('login', views.login_view, name='login'),
	path('logout', views.logout_view, name='logout')
]