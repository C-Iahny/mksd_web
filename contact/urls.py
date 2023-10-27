from django.urls import path
from .views import Kontact, About, Impressum, Anmeldebogen, uber_uns, faq



urlpatterns = [
	path('contact/', Kontact, name="contact"), 
	path('about/', About.as_view(), name="about"), 
	path('impressum/', Impressum.as_view(), name="impressum"), 
	path('anmeldebogen/', Anmeldebogen, name="anmeldebogen"), 
	path('uber_uns/', uber_uns, name="uber_uns"), 
	path('faq/', faq, name="faq"), 


]










