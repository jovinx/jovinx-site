from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='name'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('services', views.service, name='services'),
    path('services/<int:pk>', views.service_detail, name='service_detail'),
    path('forms/service_request', views.service_request, name='service_request'),
    path('forms/message', views.client_message, name='client_message'),
    path('news_letter_subscription', views.newsletter_sub, name='newsletter_sub'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)