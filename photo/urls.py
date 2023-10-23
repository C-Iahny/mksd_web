from django.urls import path
from .views import AddFiles, Files_Upload, IndexView, CreateProductView, ProductDetailView, AddProductImages, ImgaeDetail




urlpatterns = [

	path('index/', IndexView.as_view(), name="index"),
	path('addproduct/', CreateProductView.as_view(), name="addproduct"),
	path('productdetail/<int:pk>/', ProductDetailView.as_view(), name="productdetail"),
	path('addimages/<int:pk>/', AddProductImages.as_view(), name="addimages"),
	path('imagedetail/<int:pk>/', ImgaeDetail.as_view(), name="imagedetail"),
	path('file_upload/', Files_Upload, name='file_upload'),
	path('addfiles/', AddFiles.as_view(), name='addfiles'),


]










