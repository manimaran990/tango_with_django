from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=64)
	post = models.TextField(max_length=500)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user')
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		first20chars = self.post[0:10]
		return f'post: {first20chars}.. by {self.user}'