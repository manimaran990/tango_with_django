from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	author = models.ForeignKey(User, null=True, on_delete= models.CASCADE, related_name='author')
	updated_on = models.DateTimeField(auto_now=True)
	task = models.CharField(max_length=64, null=False)

	def __str__(self):
		return f"{self.author} - {self.task} - {self.updated_on}"
