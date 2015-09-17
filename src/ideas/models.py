from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PostManager(models.Manager):
	def all(self):
		return super(PostManager, self).filter(publish=True)


class Category(models.Model):
	title = models.CharField(max_length=65)
	slug = models.SlugField(unique=True)
	description = models.TextField(max_length=155)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('category', args=[str(self.slug)])


class Post(models.Model):
	publish = models.BooleanField(default=False)
	author = models.ForeignKey(User)
	categories = models.ManyToManyField(Category)
	title = models.CharField(max_length=65)
	slug = models.SlugField(unique=True)
	description = models.TextField(max_length=155)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	udpdated = models.DateTimeField(auto_now=True, auto_now_add=False)
	objects = PostManager()

	class Meta:
		ordering = ['-timestamp',]\
	
	def get_previous_post(self):
		return self.get_previous_by_timestamp()

	def get_next_post(self):
		return self.get_next_by_timestamp()

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post', args=[str(self.slug)])	
		