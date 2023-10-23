from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .models import Product, Images, FileUpload
from .forms import ProductForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
	model = Product
	template_name = "index.html"
	ordering = ['-product.id']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['productlist'] = Product.objects.all()
		return context


# add product
class CreateProductView(CreateView):
	template_name = "addproduct.html"
	form_class = ProductForm 
	success_url = reverse_lazy("index")


# Product detail
class ProductDetailView(TemplateView):
	template_name = "productdetail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['productobj'] = Product.objects.get(id = self.kwargs['pk'])

		return context


# Add product images
class AddProductImages(TemplateView):
	template_name = "addimages.html"

	def post(self, *args, **kwargs):
		try:
			images = self.request.FILES.getlist('images')
			product = Product.objects.get(id = self.kwargs['pk'])

			for image in images:
				product_images = Images.objects.create(
						product = product,
						images = image

					)
			return redirect('index')
		except ValueError as e:
			print(e)
		except Product.DoesNotExist as e:
			print(e)


# Image Details
class ImgaeDetail(TemplateView):
	template_name = 'imagedetail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['images_obj'] = Images.objects.get(id = self.kwargs['pk'])

		return context


def Files_Upload(request):
	files_post = FileUpload.objects.all()
	return render(request, 'mitmachen.html', {'files_post': files_post})


class AddFiles(CreateView):
	model = FileUpload
	template_name = "addfiles.html"
	fields = '__all__' 
	success_url = reverse_lazy("file_upload")











