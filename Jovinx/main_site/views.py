from django.shortcuts import render
from .models import Service, Client, Testimony, WebGallery, GraphicsGallery, IllustrationGallery, ArtGallery, MotionGraphicsGallery


# Create your views here.

def index(request):
    services = Service.objects.all()
    clients = Client.objects.all()
    testimonies = Testimony.objects.all()
    context = {
        'services':services[0].sub_services,
        'clients':clients,
        'testimonies':testimonies
    }
    print(context)
    return render(request, 'main_site/index.html',context)

def contact(request):
    pass

def about(request):
    pass

def gallery(request):
    pass

def service(request):
    pass

