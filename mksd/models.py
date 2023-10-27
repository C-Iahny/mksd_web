from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse  
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	biographie = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
	website_url = models.CharField(max_length=255, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)


	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('mksd_home')




class Category(models.Model):
	name = models.CharField(max_length=255)
	img = models.ImageField(upload_to='cat_images/')

	def __str__(self):
		return self.name 


	def get_absolute_url(self):
		#return reverse('details', args=str(self.id))
		return reverse('mksd_home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to='images/')
	title_tag = models.CharField(max_length=255, default="add title")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#body = models.TextField()
	body = RichTextField(blank=True, null=True)
	event_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255, default='Category')
	snippets = models.CharField(max_length=255)
	likes = models.ManyToManyField(User, related_name='like_post')

	def total_likes(self):
		return self.likes.count()


	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('article-detail', args=[str(self.id)] )


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)


class PostImg(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(PostImg, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'img_cat/images/')

    def __str__(self):
        return self.post.title





class Neuigkeit(models.Model):
	neu_name = models.CharField(max_length=125)
	neu_body = RichTextField(blank=True, null=True)
	neu_file = models.FileField(upload_to='Neuigkeit')
	neu_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.neu_name

class MKSD_LIVE(models.Model):
	name = models.CharField(max_length=55)
	body = RichTextField(blank=True, null=True)
	file = models.FileField(upload_to='MKSD_LIVE')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class MKSD_000(models.Model):
	name = models.CharField(max_length=55)
	body = RichTextField(blank=True, null=True)
	file = models.FileField(upload_to='MKSD_000')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name









