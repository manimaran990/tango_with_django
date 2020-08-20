from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

	class Meta:
		model = Blog

		fields = ['title', 'post']

		widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'post': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
			}