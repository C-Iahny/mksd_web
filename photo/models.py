from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=100)
	banner = models.ImageField(upload_to="product/banner")
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('index', args=[str(self.id)] )


class Images(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	images = models.ImageField(upload_to="product/images")

	def __str__(self):
		return self.product.title


class FileUpload(models.Model):
	name = models.CharField(max_length=50)
	file = models.FileField(upload_to="files/")
	image = models.ImageField(upload_to="files/")

	def __str__(self):
		return self.name














