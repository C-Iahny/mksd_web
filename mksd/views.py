from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import TemplateView, DeleteView, UpdateView, ListView, DetailView, CreateView  
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from photo.models import Images, FileUpload, Product
from .models import Neuigkeit, MKSD_LIVE, MKSD_000



class mksd_home(TemplateView):
	model = Product, Post, Neuigkeit, MKSD_LIVE, MKSD_000
	template_name = 'mksd_home.html'

	ordering = ['-id']
	#ou aussi comme ci-dessous
	#ordering = ['-event_date']  mais ceux d'ajourd'hui, l'affichage est different

	def get_context_data(self, *args, **kargs):
		obj = []
		context = {'obj': obj } 

		cat_menu = Product.objects.all()
		post_menu = Post.objects.all()

		neuigkeit = Neuigkeit.objects.all()
		mksd_live = MKSD_LIVE.objects.all()
		mksd_000 = MKSD_000.objects.all()

		context = super(mksd_home, self).get_context_data(*args, **kargs)
		context["cat_menu"] = cat_menu
		context["post_menu"] = post_menu
		context["neuigkeit"] = neuigkeit
		context["mksd_live"] = mksd_live
		context["mksd_000"] = mksd_000
		return context


def Armut_hunger(request):
	context = {}
	return render(request, 'armut_hunger.html', context)


def Mitmachen(request):
	files_post = FileUpload.objects.all()
	context = {}
	context = {'files_post': files_post}
	return render(request, 'mitmachen.html', context)


def UberUnsView(request):
	context = {}
	return render(request, 'uber_uns.html', context)


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	ordering = ['-date_added']

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('all_post')



def PostLikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))




def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})



def CategoryView(request, cats):
	category_posts = Post.objects.filter(category__iexact=cats)
	return render(request, 'category.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})


class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

	def get_context_data(self, *args, **kargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kargs)
		context["cat_menu"] = cat_menu
		return context



class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'

	success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']



class AddPostView(CreateView):
	model = Post  
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title', 'author')

	def get_context_data(self, *args, **kargs):
		cat_menu = Category.objects.all()

		context = super(AddPostView, self).get_context_data(*args, **kargs)
		context["cat_menu"] = cat_menu
		return context


class PostDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'

	def get_context_data(self, *args, **kargs):
		cat_menu = Category.objects.all()
		context = super(PostDetailView, self).get_context_data(*args, **kargs)

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False 
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context


class HomeView(ListView):
	model = Post  
	template_name = 'home.html'

	ordering = ['-id']
	#ou aussi comme ci-dessous
	#ordering = ['-event_date']  mais ceux d'ajourd'hui, l'affichage est different

	def get_context_data(self, *args, **kargs):
		obj = []
		context = {'obj': obj } 
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kargs)
		context["cat_menu"] = cat_menu
		return context



class AllPost(ListView):
	model = Post  
	template_name = 'all_post.html'

	ordering = ['-id']
	#ou aussi comme ci-dessous
	#ordering = ['-event_date']  mais ceux d'ajourd'hui, l'affichage est different

	def get_context_data(self, *args, **kargs):
		obj = []
		context = {'obj': obj } 
		cat_menu = Category.objects.all()
		context = super(AllPost, self).get_context_data(*args, **kargs)
		context["cat_menu"] = cat_menu
		return context



#---------------- Neuigkeiten ---------------------------------

class NeuigkeitDetailView(DetailView):
	model = Neuigkeit
	template_name = 'neuigkeit_detail.html'

	def get_context_data(self, *args, **kargs):
		neu = Neuigkeit.objects.all()
		context = super(NeuigkeitDetailView, self).get_context_data(*args, **kargs)


		context["neu"] = neu
		return context

def NeuigkeitListView(request):
	neu_menu_list = Neuigkeit.objects.all()
	return render(request, 'neuigkeit_list.html', {'neu_menu_list':neu_menu_list})



def NeuigkeitView(request, neu):
	neuigkeit_posts = Neuigkeit.objects.filter(neuigkeit__iexact=neu)
	return render(request, 'neuigkeit.html', {'neu': neu.title().replace('-', ' '), 'neuigkeit_posts':neuigkeit_posts})


class AddNeuigkeitView(CreateView):
	model = Neuigkeit
	template_name = 'add_neuigkeit.html'
	fields = '__all__'

	def get_context_data(self, *args, **kargs):
		neu_menu = Neuigkeit.objects.all()
		context = super(AddNeuigkeitView, self).get_context_data(*args, **kargs)
		context["neu_menu"] = neu_menu
		return context

















