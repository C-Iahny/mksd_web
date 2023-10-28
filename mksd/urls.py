from django.urls import path
from .views import AllPost, mksd_home, Armut_hunger, Mitmachen, UberUnsView, PostLikeView, CategoryListView, DeletePostView, UpdatePostView, AddPostView, HomeView, PostDetailView, AddCategoryView, CategoryView, AddCommentView

#AddProductImagesView, NeuigkeitDetailView, 



urlpatterns = [
	path('', mksd_home.as_view(), name="mksd_home"),
	path('all_post/', AllPost.as_view(), name="all_post"),
	path('home/', HomeView.as_view(), name='home'),
	path('article/<int:pk>', PostDetailView.as_view(), name='article-detail'),
	#path('neu/<int:pk>', NeuigkeitDetailView.as_view(), name='neu-detail'),
	path('add_post/', AddPostView.as_view(), name='add_post'),
	path('add_category/', AddCategoryView.as_view(), name='add_category'),
	path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
	path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
	path('category/<str:cats>/', CategoryView, name='category'),
	path('category_list/', CategoryListView, name='category-list'),
	path('like/<int:pk>', PostLikeView, name='like_post'),
	path('article<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
	path('mitmachen/', Mitmachen, name='mitmachen'),
	path('uber_uns/', UberUnsView, name='uber_uns'),
	path('armut_hunger/', Armut_hunger, name='armut_hunger'),



]
