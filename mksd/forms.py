from django import forms 
from .models import Post, Category, Comment


#choix = [('option', 'option'), ('sport', 'sport'), ('culture', 'culture')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippets', 'header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Safidy titra'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'Ihany', 'type': 'hidden'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippets': forms.Textarea(attrs={'class': 'form-control'}),
		} 


class EditForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title', 'title_tag', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soraty eto ny lohateny'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

		} 


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		} 



















